# FastAPI MVC Backend Template

A production-ready FastAPI backend template built using the **MVC (Model–View–Controller)** architectural pattern, designed for scalable, maintainable, and real-world backend applications.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)

---

## 🎯 Project Overview

This is a starter template for building FastAPI applications following clean architecture principles. It provides a solid foundation for:

- ✅ Starter template for FastAPI projects
- ✅ Portfolio projects
- ✅ Freelance / client-ready backend applications

---

## ✨ Features

- **Clean MVC Architecture** - Organized separation of concerns
- **Fully Async-Ready** - Built for high-performance async operations
- **JWT Authentication** - Secure token-based authentication
- **Input Validation** - Pydantic v2 schema validation
- **MongoDB Integration** - NoSQL database support
- **Error Handling** - Comprehensive exception management
- **Scalable Structure** - Ready for enterprise-level projects
- **API Documentation** - Auto-generated Swagger UI

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Framework** | FastAPI |
| **Language** | Python 3.10+ |
| **Database** | MongoDB / PostgreSQL |
| **ORM** | SQLAlchemy (Async) |
| **Validation** | Pydantic v2 |
| **Authentication** | JWT (OAuth2) |
| **Caching** | Redis |
| **Task Queue** | Celery |
| **Server** | Uvicorn / Gunicorn |
| **API Docs** | Swagger UI / ReDoc |

---
### backend folder structure 

backend-template/
│
├── app/                         # Application entry & setup
│   ├── __init__.py
│   ├── main.py                  # App entry point (uvicorn runs this)
│   ├── server.py                # FastAPI app creation
│   └── routes_register.py       # Route registration
│
├── config/                      # Configuration
│   ├── __init__.py
│   └── db.py                    # Database connection (Mongo / SQL)
│
├── core/                        # Core shared utilities
│   ├── __init__.py
│   ├── core.py                  # Settings / env loader
│   ├── dependency.py            # Common dependencies (JWT, DB)
│   └── messages.py              # ✅ Centralized messages (ADD THIS)
│
├── models/                      # DB models
│   ├── __init__.py
│   └── users.py                 # User DB model
│
├── schemas/                     # Request/Response schemas (ADD)
│   ├── __init__.py
│   └── user_schema.py           # Pydantic schemas
│
├── controllers/                 # Business logic
│   ├── __init__.py
│   └── user_controller.py
│
├── routes/                      # API routes
│   ├── __init__.py
│   ├── v1/                      # API versioning (OPTIONAL BUT PRO)
│   │   ├── __init__.py
│   │   └── user_routes.py
│
├── tests/                       # Test cases
│   ├── __init__.py
│   └── test_user.py
│
├── venv/                        # Virtual environment (ignored)
├── .env                         # Environment variables (ignored)
├── .env.example                 # Env template
├── .gitignore
├── README.md
├── requirements.txt
├── setup.bat
└── run.bat



## 🏗️ Architecture Pattern: MVC

| Layer | Purpose | Location |
|-------|---------|----------|
| **Model** | Database schemas & data validation | `models/` |
| **View** | API responses & JSON formatting | `routes/` |
| **Controller** | Business logic & data operations | `controllers/` |

### Flow Diagram

```
Request → Routes → Controller → Model → Database
Response ← Routes ← Controller ← Model ← Database
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- MongoDB running locally or configured via `.env`
- Windows OS (for `.bat` scripts)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd backend-template
   ```

2. **Run setup script** (Windows)
   ```bash
   setup.bat
   ```
   This will:
   - Create a virtual environment
   - Activate the virtual environment
   - Install dependencies from `requirement.txt`

3. **Configure environment variables**
   ```bash
   copy .env.example .env
   ```
   Update `.env` with your configuration

4. **Run the server**
   ```bash
   run.bat
   ```
   The API will be available at `http://127.0.0.1:8000`

5. **Access API Documentation**
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

---

## 📡 API Endpoints

### User Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| **GET** | `/users/` | Welcome message & API home |
| **POST** | `/users/create` | Create a new user |

### Request/Response Examples

**Create User (POST)**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "SecurePass123!"
}
```

**Response (Success)**
```json
{
  "message": "User created successfully"
}
```

---

## 🔐 Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Application Settings
APP_NAME=FastAPI MVC Backend
APP_ENV=development
DEBUG=true
PORT=8000

# Database
MONGO_URL=mongodb://localhost:27017
MONGO_DB_NAME=fastapi_db

# Security
JWT_SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256

# Email Configuration
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-email-password
```

---

## 📋 Input Validation Rules

### User Creation Validation

- **Name**: Letters and spaces only
- **Email**: Valid email format required
- **Password**: 
  - 8-20 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character
  - Must start with uppercase letter

---

## 📦 Dependencies

Core packages:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `pydantic>=2.6` - Data validation
- `pymongo>=4.6` - MongoDB driver
- `sqlalchemy>=2.0` - ORM
- `python-jose` - JWT authentication
- `passlib[bcrypt]` - Password hashing
- `email-validator` - Email validation

See [requirement.txt](requirement.txt) for the complete list.

---

