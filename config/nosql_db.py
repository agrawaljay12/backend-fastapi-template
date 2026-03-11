from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGODB_URL")
DB_NAME = os.getenv("MONGODB_DB_NAME")

client = MongoClient(MONGO_URL)

mongo_db = client[DB_NAME]

def get_mongo_db():
    return mongo_db