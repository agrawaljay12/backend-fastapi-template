# import the passlib library for password hashing
import hashlib
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Load environment variables for JWT configuration
jwt_secret_key = os.getenv("JWT_SECRET_KEY")
jwt_algorithm = os.getenv("JWT_ALGORITHM")
access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# create a CryptContext object for hashing passwords
pwd_context = CryptContext(schemes=["argon2"],deprecated="auto")


# ---------------------password hashing functions ---------------------

# add the hash password function for plain text password hashing
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# add the verify password function for plain text and hashed password comparison
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# --------------------- JWT token functions ---------------------

# create access token function for  generate jwt token creation
def create_access_token(data:dict):  #

    # Create a copy of the input data to avoid modifying the original dictionary
    to_encode = data.copy()

    # Set the expiration time for the token
    expire = datetime.now(timezone.utc) + timedelta(minutes=access_token_expire_minutes)

    # # Add the expiration timestamp to the token payload
    to_encode.update({"exp": expire})

    # Encode the token with the secret key and algorithm
    encoded_jwt = jwt.encode(to_encode, jwt_secret_key, algorithm=jwt_algorithm)

    # Return the encoded JWT token
    return encoded_jwt

# Verify and decode JWT token
def verify_token(token: str) -> dict:
    """
    Decode and verify JWT token validity
    Args:
        token: JWT token string from request header
    Returns:
        Decoded token payload containing user information
    Raises:
        JWTError: If token is invalid or expired
    """
    try:
        payload = jwt.decode(token, jwt_secret_key, algorithms=[jwt_algorithm])
        return payload
    except JWTError as e:
        raise JWTError(f"Token validation failed: {str(e)}")


    # refresh token function for generating new jwt token before expiration
def refresh_access_token(token: str) -> str:
    try:
        # Decode the existing token to get its payload
        payload = jwt.decode(token, jwt_secret_key, algorithms=[jwt_algorithm])

        # Remove the expiration field to create a new token
        payload.pop("exp", None)

        # Create a new access token with updated expiration
        new_token = create_access_token(payload)

        return new_token
    except JWTError as e:
        raise JWTError(f"Token refresh failed: {str(e)}")