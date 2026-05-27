from fastapi import Request
from service.otp_service import send_otp, verify_otp

async def send_otp_controller(request:Request):
    data = await request.json()
    email = data.get("email")
    return send_otp(email)

async def verify_otp_controller(request:Request):
    data = await request.json()
    email = data.get("email")
    otp = data.get("otp")
    return verify_otp(email,otp)
