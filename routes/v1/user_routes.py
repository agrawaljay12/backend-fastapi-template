from fastapi import APIRouter,Request, HTTPException,status
from controllers.user_controller import create_user,login_user
from models.users import User
from fastapi.responses import JSONResponse
import re

router = APIRouter()

# url: http://127.0.0.1:8000/users/
# method: GET
# description : WELCOME TO API HOME 
@router.get('/',response_description="Welcome to the User Management API")
async def home():
    return JSONResponse(
        status_code= status.HTTP_200_OK,
        content={"message": "Welcome to the User Management API"}

    )

# URL:http://127.0.0.1:8000/api/v1/users/create
# method : POST
# description : create a new user

@router.post("/create",response_description="Create a new user")
async def add_user(request:Request):
    return await create_user(request)


# URL: http://127.0.0.1:8000/api/v1/users/login
# method : POST
# description : login a user

@router.post("/login",response_description="Login a user")
async def handle_login_user(request:Request):
   return await login_user(request)
