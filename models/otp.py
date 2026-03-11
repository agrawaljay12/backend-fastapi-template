from pydantic import BaseModel


class OTP(BaseModel):
    email: str
    otp: str
    created_at: float  # timestamp when OTP was created
    expires_at: float  # OTP expiry time in secondsa




