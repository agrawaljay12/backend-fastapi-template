# from streamlit import user
import re
from config.db import db 
from models.users import User
from fastapi import HTTPException, Request ,status
from bson import ObjectId 
from typing import List,Dict
from core.core import hash_password,verify_password,create_access_token
from datetime import datetime, timedelta

user_collection = db["users_database"]


# create a new user function
async def create_user(request:Request):
    
    try:
        # get the json data from request body
        data = await request.json()
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        # validation for all required fields

        if not name or not email or not password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail = "Name, email and password are required fields"
            )
        
        # validate name format
        if not re.match(r'^[a-zA-Z ]+$', name):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Name must contain only letters"
                )
            
        # validate email format
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid email format"
                )
            
        # validate password format
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[A-Z][A-Za-z\d\W_]{7,15}$'
        if not re.match(password_pattern, password):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Password must be between 8 and 20 characters"
                )
            

        #  check the user if already exists with the same email then return error message.
        user = user_collection.find_one({"email":data["email"]})
        if user:
                raise HTTPException(
                    status_code = status.HTTP_400_BAD_REQUEST,
                    detail = "User with this email already exists"
                )

        # convert the plain password to hashed password before storing in database that user entered
        hashed_password = hash_password(password) 

        # insert the user data into the database
        result = user_collection.insert_one({
                  "name":name,
                  "email":email,
                  "password": hashed_password,
                  "role":"user"  # default role is 'user'   
             })

        # if data is inserted successfully then return success message and user id
        return ({
            "message":"User created successfully",
            "user_id": str(result.inserted_id)
        })
     
    #  catch any exception that occurs during the process and raise HTTPException
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = str(e)
        )

    # login user function

async def login_user(request:Request):
     try:
        # get the json data from request body
        data = await request.json()
        email = data.get('email')
        password = data.get('password')
    

        # validation for email and password fields
        if not email or not password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email and password are required fields"
            )
        
        # validate the email format
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email format"
            )
        
        # # validate password format
        # password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[A-Z][A-Za-z\d\W_]{7,15}$'
        # if not re.match(password_pattern, password):
        #         raise HTTPException(
        #             status_code=status.HTTP_400_BAD_REQUEST,
        #             detail="Password must be between 8 and 20 characters"
        #         )
            
        
        #  check the user if exists with the given email or not if not then return error message. 
        user = user_collection.find_one({"email":email})
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        # verify the plain password with hashed password stored in database 
        is_password_valid  = verify_password(password,user['password'])
        
        if not is_password_valid:
            raise HTTPException(
                status_code= status.HTTP_400_BAD_REQUEST,
                detail="Invalid password"
            )
        
        token_data = {
            "user_id": str(user["_id"]),
            "email": user["email"],
            "name": user["name"],
            "role": user["role"]
        }

        access_token = create_access_token(token_data)

        # if user is found and password is correct and hashed then return user data    
        return ({
            "message":"Login Successful",
            "access_token": access_token,
            "token_type": "bearer",
            "user":token_data
        })
     
    #  catch any exception that occurs during the process and raise HTTPException
     except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
          

# get all users function

async def get_all_users() -> list[dict]:
    try:
        users = []
        for user in user_collection.find({}):
            users.append({
                "_id": str(user["_id"]),
                "name": user["name"],
                "email": user["email"],
                "role": user.get("role", "user")
            })
        return users
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
