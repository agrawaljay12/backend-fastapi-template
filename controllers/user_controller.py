from config.db import db 
from models.users import User
from fastapi import HTTPException ,status
from bson import ObjectId 

user_collection = db["users_database"]

def create_user(user:User):
    try:
        user_data = user.dict()
        if user_collection.find_one({"email":user_data["email"]}):
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "User with this email already exists"
            )
        result = user_collection.insert_one(user_data)
        return True if result.inserted_id else False
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = str(e)
        )