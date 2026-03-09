import os 
from config.sql_db import get_sql_db
from config.nosql_db import get_mongodb_db
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

db_type = os.getenv("DB_TYPE")

def get_database():

    if db_type == "mongodb":
        return get_mongodb_db()

    elif db_type == "postgres":
        return get_sql_db()

    elif db_type == "mysql":
        return get_sql_db()

    elif db_type == "sqlite":
        return get_sql_db()

    else:
        raise Exception("Invalid Database Type")
