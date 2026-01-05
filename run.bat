:: venv\Scripts\activate && server.py

:: Activate virtual environment
call venv\Scripts\activate

:: Run FastAPI server
uvicorn app.main:app --reload
