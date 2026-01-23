import uuid
from fastapi.testclient import TestClient
from app.main import app

# # from models.users import User
# import routes.version.v1.user_routes as user_router

client = TestClient(app)

# test case for create user endpoint
def test_create_user_success():
    data = {
        "name": "Test User",
        "email": f"test_{uuid.uuid4()}@gmail.com",
        "password": "Test@1234"
    }

    response = client.post("/api/v1/users/create", json=data)

    assert response.status_code == 201 # check HTTP status code with returned status code
    assert response.json()["status"] == 201 # check status code in response body
    assert response.json()["message"] == "User created successfully"
    assert "user_id" in response.json()["data"]

# test case for Invalid password format ,email format ,Invalid name format , Invalid email already exists
def test_create_user_invalid_email_format():

    data ={
        "name": "Test User",
        "email": "testgmail.com",
        "password": "Test@1234"
    }

    response = client.post("/api/v1/users/create",json=data)

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid email format"

def test_create_user_invalid_name_format():

    data ={
        "name": "test user123",
        "email": "test@gmail.com",
        "password": "Test@1234"
    }

    response = client.post("/api/v1/users/create",json=data)

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid name format"

def test_create_user_invalid_password_format():

    data ={
        "name": "test user",
        "email": "test@gmail.com",
        "password": "test@1234"
    }

    response = client.post("/api/v1/users/create",json=data)

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid password format"
  
#  test case for login user endpoint
def test_login_success():

    # STEP 1: Create user
    create_payload = {
        "name": "Jay Test",
        "email": "jay@test.com",
        "password": "Jay@12345"
    }
    client.post("/api/v1/users/create", json=create_payload)

    # STEP 2: Login user
    login_payload = {
        "email": "jay@test.com",
        "password": "Jay@12345"
    }
    response = client.post("/api/v1/users/login", json=login_payload)

    assert response.status_code == 200
    assert response.json()["status"] == 200  # Check status in body
    assert response.json()["message"] == "Login Successful"
    assert "access_token" in response.json()["data"]
# test case for Invalid login

def test_login_invalid_password():

    # Create user first
    client.post("/api/v1/users/create", json={
        "name": "Jay Test",
        "email": "jay@test.com",
        "password": "Jay@12345"
    })

    # Try wrong password
    response = client.post("/api/v1/users/login", json={
        "email": "jay@test.com",
        "password": "Wrong@123"
    })

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid password"
