* A production-ready FastAPI backend template built using the MVC (Model–View–Controller) architectural pattern, designed for scalable, maintainable, and real-world backend applications.

This repository can be used as:

1. A starter template for FastAPI projects

2. A portfolio project

3. A freelance / client-ready backend base

* Key Highlights

1. Clean MVC architecture

2. Fully async-ready

3. JWT authentication

4. Scalable project structure

5. Production & GitHub friendly

* Tech Stack

Backend Framework: FastAPI

Language: Python 3.10+

ORM: SQLAlchemy (Async)

Database: PostgreSQL / MongoDB (configurable)

Auth: JWT (OAuth2 Password Flow)

Validation: Pydantic v2

Caching: Redis

Background Tasks: Celery

API Docs: Swagger UI / ReDoc

Server: Uvicorn / Gunicorn

Containerization: Docker

* Architecture (MVC Pattern)

| Layer          | Responsibility                 |
| -------------- | ------------------------------ |
| **Model**      | Database tables and ORM models |
| **Schema**     | Request & response validation  |
| **Controller** | API routes (HTTP layer)        |
| **Service**    | Business logic                 |


* Templates Structure 

fastapi-mvc-backend/
│
├── app/
│   ├── main.py                # Application entry point
│   ├── routes.py              # Route registry
│
│   ├── core/                  # Core configurations
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── dependencies.py
│   │   └── logger.py
│
│   ├── models/                # Database models (M)
│   ├── schemas/               # Pydantic schemas
│   ├── controllers/           # API controllers (C)
│   ├── services/              # Business logic
│   ├── repositories/          # DB operations
│   ├── middlewares/           # Custom middlewares
│   ├── utils/                 # Utility helpers
│   └── db/                    # Database sessions & base
│
├── alembic/                   # Database migrations
├── tests/                     # Unit & integration tests
│
├── .env.example               # Environment variable template
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md



