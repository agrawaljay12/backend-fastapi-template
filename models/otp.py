from pydantic import BaseModel

class OTP(BaseModel):
    email: str
    otp: str
    created_at: str # timestamp when OTP was created
    expires_at: str  # OTP expiry time in secondsa




