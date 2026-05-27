from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi import status
from controllers.otp_controller import send_otp_controller, verify_otp_controller

router = APIRouter()

# url: http://localhost:8000/api/v1/otp/
# method: GET
# description : WELCOME TO API HOME 
@router.get('/',response_description="Welcome to the OTP Management API")
async def home():
    return JSONResponse(
        status_code= status.HTTP_200_OK,
        content={"message": "Welcome to the OTP Management API"}

    )


# http://localhost:8000/api/v1/otp/send
# Method:POST
# description: generate the otp 
@router.post("/send",description="generate the otp")
async def generate_otp_endpoint(request:Request):
    return await send_otp_controller(request)


# http://localhost:8000/api/v1/otp/verify
# Method:DELETE 
# description: verify the otp
@router.delete("/verify",description="verify the otp")
async def verify_otp_endpoint(request:Request):
    return await verify_otp_controller(request)



