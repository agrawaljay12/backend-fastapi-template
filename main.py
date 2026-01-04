#  here all the routes are register 

from fastapi import FastAPI
from routes.user_routes import router as user_router 

app = FastAPI()

# http://127.0.0.1:8000/users/
app.include_router(user_router, prefix="/users",tags=["users"])

