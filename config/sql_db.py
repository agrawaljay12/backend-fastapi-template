from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

def get_sql_db():

    DATABASE_URL = os.getenv("POSTGRESQL_URL")

    if not DATABASE_URL:
        raise ValueError("POSTGRESQL_URL not found in .env")

    engine = create_engine(DATABASE_URL)

    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    db = SessionLocal()

    try:
        return db
    finally:
        db.close()