import os
from dotenv import load_dotenv
from config.nosql_db import get_mongo_db

if("ENVIRONMENT") == "development":
    load_dotenv(".env.development")
else:
    load_dotenv()

DB_TYPE = os.getenv("DB_TYPE")

def get_database():

    if DB_TYPE == "mongodb":
        return get_mongo_db()

    elif DB_TYPE in ["postgresql", "mysql", "sqlite"]:
        from config.sql_db import get_sql_db
        return get_sql_db()

    else:
        raise Exception("Invalid DB_TYPE")