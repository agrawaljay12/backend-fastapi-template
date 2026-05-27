# from streamlit import user
from fastapi import File, Form, Request, UploadFile
from service.user_service import create_user_service, get_all_users_service, login_user_service

# create a new user function
async def create_user(
    name:str = Form(...),
    email:str=Form(...),
    password:str = Form(...),
    file:UploadFile = File(None)
):
    
    return await create_user_service(
        name = name,
        email=email,
        password= password,
        file=file
    )


# login user function
async def login_user(request:Request):
    data = await request.json()
    email = data.get('email')
    password = data.get('password')
    return login_user_service(email,password)
     
# get all users function
async def get_all_users() -> list[dict]:
    return get_all_users_service()
   
