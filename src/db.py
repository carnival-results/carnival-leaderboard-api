import os
from pymongo import MongoClient


def create_mongo_client():
    client = MongoClient(os.getenv("MONGO_URL"))
    return client[os.getenv("MONGO_DB")]
