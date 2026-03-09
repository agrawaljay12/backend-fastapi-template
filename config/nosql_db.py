from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Load environment variables from .env file
mongodb_url =  os.getenv("mongodb_url")
mongodb_name = os.getenv("mongodb_name", "fastapi_db")

# Initialize MongoDB client and database
client = MongoClient(mongodb_url)
db = client[mongodb_name]

# function to get the MongoDB database instance
def get_mongodb_db():
    return db





