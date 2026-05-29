@echo off

IF NOT EXIST venv (
    echo Virtual environment not found!
    echo Please run setup.bat first.
    pause
    exit
)

call venv\Scripts\activate

uvicorn app.main:app --reload