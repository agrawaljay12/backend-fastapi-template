from fastapi.responses import JSONResponse
from config.db_factory import get_database
from core.validation import validate_email
from core.response import created_response,success_response,error_response
from core import message,http_status
from models.otp import OTP
from fastapi import status,HTTPException
import random 
from datetime import datetime,timedelta
from utils.mail import send_email
from utils.otphtml import send_otp_html

db = get_database()

otp_collection = db["otp"]
user_collection = db["users"]

def send_otp(email:str):
    try:
       
        # Validate email format
        if not email or not isinstance(email, str):
            raise HTTPException(status_code=400, detail="Email is required")

        # Email validation 
        validate_email(email)

        # check the user is exist or not 

        user = user_collection.find_one({"email":email})

        if not user:
            raise HTTPException(
                status_code=http_status.NOT_FOUND,
                detail=message.USER_NOT_FOUND
            )

        # generate a random 6-digit OTP
        otp = str(random.randint(100000, 999999))

        # set the OTP expiration time (e.g., 10 minutes from now)
        expires_at = datetime.utcnow() + timedelta(minutes=10)
        created_at=datetime.utcnow().isoformat()

        # create an Otp object and save it to the database
        otp_data = OTP(email=email, otp=otp, created_at=created_at, expires_at=expires_at.isoformat())
        otp_collection.insert_one(otp_data.dict())

        # send the OTP to the user's email
        email_body = send_otp_html(otp)
        send_email(to_email=email, subject="Your OTP Code", body=email_body)

        # return created_response(
        #     status_code=status.HTTP_201_CREATED,
        #     content={
        #         "status":"201",
        #         "message": "OTP generated and sent to email successfully"
        #     }
        # )
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "status":"201 Created",
                "message":"Otp is Sent to email"
            }
        )
    
    except HTTPException:
        raise

    except Exception as e:
       return error_response(
           status=http_status.INTERNAL_SERVER_ERROR,
           message=str(e)
       )

# verify otp service
def verify_otp(email:str,otp:str):
    try:
        if not email or not otp:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="email and otp is required"
            )
        
        validate_email(email)
        
        # check the email exist or not 
        if not otp_collection.find_one({"email":email}):
             raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="email is not found"
            )
        
        otp_record = otp_collection.find_one({"email":email,"otp":otp})

        if not otp_record:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail= "Invalid otp"
            )
        
        expire_at = otp_record.get("expire")

        # parse the datetime iso string to datetime 
        if isinstance(expire_at,str):
            expire_at = datetime.fromisoformat(expire_at)
    
        if expire_at is not None:
            if datetime.utcnow() > expire_at:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="otp is expired"
                )
        
        # delete after the verification
        otp_collection.delete_one({"_id":otp_record["_id"]})

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "status":"200 OK",
                "message":"Otp is Verified"
            }
        )
    
    except HTTPException as e:
        raise e
    
    except Exception as e:
       return error_response(
           status=http_status.INTERNAL_SERVER_ERROR,
           message=str(e)
       )       