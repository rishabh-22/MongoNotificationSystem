import os
import pymongo

client = pymongo.MongoClient(os.environ['STREAM_DB'])
print(client.changestream.collection.insert_one({"hello": "world"}).inserted_id)
