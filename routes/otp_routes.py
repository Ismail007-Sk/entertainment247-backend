from database.database import SessionLocal
from services import otp_service,email_service
from fastapi import APIRouter,HTTPException
from schemas.otp_schemas import ForgotPasswordRequest
from models.user_registration_model import User


router = APIRouter()

@router.post("/forgot_password")
def forgot_password(data:ForgotPasswordRequest):
    db = SessionLocal()

    # Check user exists in main user_table or not
    user_existed = db.query(User).filter(User.email==data.email).first()

    if not user_existed:
        raise HTTPException(
            status_code=401,
            detail="Email Not Found"
        )
    
    # Generate OTP
    generated_otp = otp_service.generate_otp()
    print(f"OTP GENERATED IN BACKEND {generated_otp}")
    # OTP saved to otp_table
    otp_service.save_otp(db,data.email,generated_otp)
    print("OTP SAVED IN DATABASE")

    # Sending OTP Email
    # email_service.sent_otp_email(data.email,generated_otp) 

    
    return {
        "message": "OTP has been sent successfully.",
        "otp":generated_otp
    }






