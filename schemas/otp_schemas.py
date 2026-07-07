from pydantic import BaseModel,EmailStr,Field


class ForgotPasswordRequest(BaseModel):
    email:EmailStr


class ResetPasswordRequest(BaseModel):
    email:EmailStr 
    otp:str = Field(min_length=6,max_length=6,description ="6-digit OTP")
    new_password : str

class PasswordVerify(BaseModel):
    password:str