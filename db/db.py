import csv

from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
CONNECTION_STRING = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")


def backup_products(file):
    client = MongoClient(CONNECTION_STRING)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    with open(file, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] == "MTM" and row[1] == "SN":
                continue
            item = {'MTM': row[0],
                    'SN': row[1]}
            collection.update_one(item, {"$set": item}, upsert=True)
