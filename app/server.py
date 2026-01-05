from fastapi import FastAPI

def create_server() -> FastAPI:
    app = FastAPI(
        title="Backend API",
        version="1.0.0"
    )
    return app
