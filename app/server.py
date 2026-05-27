from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
def create_server() -> FastAPI:
    app = FastAPI(
        title="Backend API",
        version="1.0.0"
    )

     # add cors origin middleware 
    origins=[
            "http://localhost:5173",      # Frontend dev server
            "http://127.0.0.1:5173",      # Alternative localhost
            "http://localhost:3000",      # Alternative port
            "http://127.0.0.1:3000",      # Alternative localhost:3000
        ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins= origins,
        allow_credentials = True,
        allow_methods =["*"],
        allow_headers=["*"]
    )

    # add static files from directory automatically using sttaticfiles
    app.mount("/static",StaticFiles(directory="static"),name="static")
    return app

   


