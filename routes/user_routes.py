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

# http://127.0.0.1:8000/users/create
# method : POST
# description : create a new user

@router.post("/create",response_description="Create a new user")
async def add_user(request:Request):
    try:
        data = await request.json()
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        # do the validation of required fields
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[A-Z][A-Za-z\d\W_]{7,15}$'
        pattern = r'^[a-zA-Z ]+$'
        if not name or not email or not password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Name, email and password are required fields"
            )
        if not re.match(pattern, name):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Name must contain only lowercase letters"
            )
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email format"
            )
        if not re.match(password_pattern, password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must be between 8 and 20 characters"
            )
        user = User(name=name, email=email, password=password)
        result = create_user(user)
        if result:
            return JSONResponse(
                status_code=201,
                content={"message": "User created successfully"}
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

# http://127.0.0.1:8000/users/login
# method : POST
# description : login a user

@router.post("/login",response_description="Login a user")
async def handle_login_user(request:Request):
    try:
        # get the json data from request body
        data = await request.json()
        email = data.get("email")
        password = data.get("password")

        """call the instance of login_user function from user_controller.py
        and pass email and password to it and return the result as json response"""
        result = login_user(email,password)
        if result:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=result
            )
    
    # exception handling exceptions occurs during the process and raise HTTPException
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )