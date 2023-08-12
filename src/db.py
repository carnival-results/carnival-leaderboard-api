import os
from pymongo import MongoClient


def create_mongo_connection(collection):
    client = MongoClient(os.getenv("MONGO_URL"))
    client[os.getenv("MONGO_DB")]

    return client.db[collection]
