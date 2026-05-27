from pydantic import BaseModel 

class User(BaseModel):
    name:str
    email:str
    password:str
    role:str = "user"  # default role is 'user'
    profile:str ="http://localhost:8000/users/uploads/default.png" 

