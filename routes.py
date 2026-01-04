"""all the routes can be register here"""
from routes.user_routes import router as user_router
from fastapi import FastAPI
app = FastAPI()

app.include_router(user_router, prefix="/users",tags=["users"])