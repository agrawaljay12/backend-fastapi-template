# from streamlit import user
from config.db import db 
from models.users import User
from fastapi import HTTPException ,status
from bson import ObjectId 
from core.core import hash_password,verify_password

user_collection = db["users_database"]


# create a new user function
def create_user(user:User):
     user_data = user.dict()

    #  check the user if already exists with the same email then return error message.
     if user_collection.find_one({"email":user_data["email"]}):
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "User with this email already exists"
            )
     try:

        # convert the plain password to hashed password before storing in database that user entered
        user_data["password"] = hash_password(user_data["password"]) 

        # insert the user data into the database
        result = user_collection.insert_one(user_data)

        # if data is inserted successfully then return True
        return True if result.inserted_id else False
     
    #  catch any exception that occurs during the process and raise HTTPException
     except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = str(e)
        )

    # login user function

def login_user(email:str,password:str): 
     try: 
        #  check the user if exists with the given email or not if not then return error message. 
        user  =  user_collection.find_one({"email":email})
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        # verify the plain password with hashed password stored in database 
        is_password_valid  = verify_password(password,user['password'])
        
        if not is_password_valid:
            raise HTTPException(
                status_code= status.HTTP_404_BAD_REQUEST,
                detail="Invalid password"
            )

        # if user is found and password is correct and hashed then return user data    
        return ({
            "message":"Login Successful",
            "user":{
                "_id":str(user["_id"]),
                "name":user["name"],
                "email":user["email"]
            }
        })
     
    #  catch any exception that occurs during the process and raise HTTPException
     except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
          
     
   
