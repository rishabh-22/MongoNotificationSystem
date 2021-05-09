import csv
import os
import pymongo
import smtplib
import ssl
from bson.json_util import dumps


def get_receivers(file):
    emails = []
    flag = True

    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if flag:
                flag = False  # to skip the heading row
                continue
            emails.append(row[0])  # assuming first column of the csv contains emails

    return emails


def send_email(data, emails):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = os.environ['EMAIL']
    password = os.environ['PASSWORD']
    message = f"""\
    Subject: Hi there
    These are the changes observed in the database.

    {data}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        for email in emails:
            server.sendmail(sender_email, email, message)


client = pymongo.MongoClient(os.environ['STREAM_DB'])
change_stream = client.changestream.collection.watch()
receivers = get_receivers('emails.csv')

for change in change_stream:
    print(dumps(change), end='\n\n')
    send_email(dumps(change), receivers)
