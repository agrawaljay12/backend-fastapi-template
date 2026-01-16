from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# test case for create user endpoint
def test_create_user_success():

    data ={
        "name": "Test User",
        "email": "test@gmail.com",
        "password": "Test@1234"
    }

    response = client.post("/api/v1/users/create",json=data)
    
    assert response.status_code == 200
    assert response.json()["message"] == "User created successfully"

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
    payload = {
        "email": "jay@test.com",
        "password": "Jay@12345"
    }

    response = client.post("/users/login", json=payload)

    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Login Successful" 

# test case for Invalid login

def test_login_invalid_password():
    payload = {
        "email": "jay@test.com",
        "password": "Wrong@123"
    }

    response = client.post("/users/login", json=payload)

    assert response.status_code == 404
    assert response.json()["detail"] == "Invalid password and email"