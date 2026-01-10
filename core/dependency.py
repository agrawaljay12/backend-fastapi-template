from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import os


oauth2_scheme =  OAuth2PasswordBearer(tokenUrl="/users/login")

# Load environment variables for JWT configuration
jwt_secret_key = os.getenv("JWT_SECRET_KEY")
jwt_algorithm = os.getenv("JWT_ALGORITHM")

# create get current user function for extracting and verifying jwt token from request
def get_current_user(token:str=Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, jwt_secret_key, algorithms=[jwt_algorithm])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    
def get_active_user(current_user:dict=Depends(get_current_user)):
    if not current_user.get("is_active", False):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user