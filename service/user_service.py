from config.db_factory import get_database
from models.users import User
from fastapi import HTTPException
from core.core import hash_password,verify_password,create_access_token
from core import message
from core import http_status
from core import response
from core import validation
from fastapi import UploadFile,Form,File
from utils.file_upload import save_file

db = get_database()

user_collection = db["users"]

# create a new user function
async def create_user_service(
        name:str = Form(...),
        email:str=Form(...),
        password:str = Form(...),
        file:UploadFile = File(None)
):
    try:


        # -----------------validate input fields-------------------
        # validate all required fields
        # validation.validate_data(name,email,password)

        # validate name format
        validation.validate_name(name)

        # validate email format
        validation.validate_email(email)

        # validate password format
        validation.validate_password(password)

        #  check the user if already exists with the same email then return error message.
        if user_collection.find_one({"email":email}):
            raise HTTPException(
                status_code = http_status.BAD_REQUEST,
                detail = message.USER_ALREADY_EXISTS
            )

        # convert the plain password to hashed password before storing in database that user entered
        hashed_password = hash_password(password) 

        if file:
            profile = await save_file(file)
        else:
            profile ="http://localhost:8000/users/upload/default.png"

        # insert the user data into the database
        user_data = User(
            name=name,
            email=email,
            password=hashed_password,
            profile=profile
        )
        result = user_collection.insert_one(user_data.model_dump())

        # if data is inserted successfully then return success message and user id
        return response.created_response(
            message=message.USER_CREATED_SUCCESS,
            data={"user_id": str(result.inserted_id)}
        )
     
    # Re-raise validation errors
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=http_status.INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    

# login user function
def login_user_service(email:str,password:str):
    try:
        # validation for email and password fields
        if not email or not password:
            raise HTTPException(
                status_code=http_status.BAD_REQUEST,
                detail=message.REQUIRED_FIELDS_MISSING
            )
        
        # validate email format
        validation.validate_email(email)   
        
        #  check the user if exists with the given email or not if not then return error message. 
        user = user_collection.find_one({"email":email})
        if not user:
            raise HTTPException(
                status_code=http_status.NOT_FOUND,
                detail=message.USER_NOT_FOUND
            )
        
        # verify the plain password with hashed password stored in database      
        if not verify_password(password,user['password']) :
            raise HTTPException(
                status_code= http_status.UNAUTHORIZED,
                detail=message.INVALID_PASSWORD
            )
        
        token_data = {
            "user_id": str(user["_id"]),
            "email": user["email"],
            "name": user["name"],
            "role": user.get("role","user")
        }

        access_token = create_access_token(token_data)

        # if user is found and password is correct and hashed then return user data  
        return response.success_response(
            message.LOGIN_SUCCESS,
            data={
                "access_token": access_token,
                "token_type": "bearer",
                "user": token_data
            }
        )  
     
     # Re-raise validation errors
    except HTTPException as e:
        raise e
    
    except Exception as e:
        raise HTTPException(
            status_code=http_status.INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    
# get all users function
def get_all_users_service() -> list[dict]:
    try:
        users = []
        for user in user_collection.find({}):
            users.append({
                "_id": str(user["_id"]),
                "name": user["name"],
                "email": user["email"],
                "role": user.get("role", "user")
            })
        return response.success_response(
            message.USER_FETCH_SUCCESS,
            data=users
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=http_status.INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
     
   

     