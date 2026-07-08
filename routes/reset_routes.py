from database.database import SessionLocal
from models.user_registration_model import User
from utils.security import hashing_password
from services import otp_service
from fastapi import APIRouter,HTTPException
from schemas.otp_schemas import ResetPasswordRequest
from services.email_service import sent_password_change_email

router = APIRouter()

@router.post("/reset_password")
def reset_password(data:ResetPasswordRequest):

    db = SessionLocal()

    # Check user exists in main user_table or not
    user_exists = db.query(User).filter(User.email==data.email).first()

    if not user_exists:
        raise HTTPException(
            status_code=404,
            detail="Email not found."
        )
    

    #Verify OTP
    otp_valid = otp_service.verify_otp(db,data.email,data.otp)

    if not otp_valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired OTP."
        )


    # Hash new password
    user_exists.password = hashing_password(data.new_password)
    # sent_password_change_email(user_exists.email)
    
    # Updating database
    db.add(user_exists)
    db.commit()

    # Deleting the otp from otp_table
    otp_service.delete_otp(db,data.email)

    return {
        "message": "Password reset successfully."
    }