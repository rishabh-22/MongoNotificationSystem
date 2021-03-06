# Mongo Notification System

### This script is used to be used as a lambda function to monitor any changes in the database collection or any field.

## Features

* alerts user regarding any change in the database.
* sends an email to the list of users who subscribe to it
* reads the list of subscribed users from a csv file

## Flow of Project

The user is required to export 3(three) environment variables:
* MongoDB uri/ connection string -> `STREAM_DB`
* email of the account which is to be used to send alerts from -> `EMAIL`
* password of the email account used for sending alerts -> `PASSWORD`
* Once the script is running, add a csv file with emails in the first column to read the mail recipients and then the `utils` file can be run to make changes to the specific database by inserting a new object. Feel free to make changes to it to test for other cases.

Also, the user is required to enable access to less secure applications in order for python SMTP client to login into the account to send alerts (in google domain)

## Flow of Logic

> 1. A client is made using the URI of the hosted MongoDB cluster
> 2. Using the client a change stream is established which is used to monitor the database and returns an iterator of changes whenever a change is detected.
> 3. List of email of all the subscribers is extracted from the CSV file. The function `get_receivers` expects the path to the csv file.
> 4. The scripts constantly monitors the DB and whenever a change is observed, it is first printed to the console and then the `send_email` function is called which sends the change notification to all the subscribers.

## TODO

Some things which I wanted to implement but couldn't due to lack of time: 
* Make this into an actual web application which would accept the emails like a subscribe-to-emails list.
* Handle the exceptions (network or other), as I didn't have much time, I could not make it as ready as production level, accomplished more of a POC with this.
* The name of the DB here is fixed (`changestream`). Would like to implement a method which will accept the name as an argument. Hence, multiple such instances could be brought up for different databases with ease. 
* I could not host the project since there's no option as of now to add new emails except updating the csv-file.

## References
I took help from the official mongo website to look up for change streams for python and stackoverflow.