from fastapi import FastAPI
from routes.user_routes import router as user_router

def register_routes(app: FastAPI):
    app.include_router(
        user_router,
        prefix="/users",
        tags=["users"]
    )


