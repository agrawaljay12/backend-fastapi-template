from pymongo import MongoClient
import os
from dotenv import load_dotenv
import certifi

if("ENVIRONMENT")=="development":
    load_dotenv(".env.development")
else:
    load_dotenv()

MONGO_URL = os.getenv("MONGODB_URL")
DB_NAME = os.getenv("MONGODB_DB_NAME")

client = MongoClient(
    MONGO_URL,
    tlsCAFile = certifi.where()
)

mongo_db = client[DB_NAME]

def get_mongo_db():
    return mongo_db