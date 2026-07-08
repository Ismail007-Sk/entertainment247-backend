from models.user_registration_model import User
from fastapi import APIRouter,HTTPException
from schemas.otp_schemas import PasswordVerify
from database.database import SessionLocal
from utils.security import hashing_password,verify_password
from services.email_service import sent_password_change_email

router = APIRouter()


@router.post("/verify_password/{id}")
def verifyPassword(id:int , data:PasswordVerify):
    db = SessionLocal()
    user_existed = db.query(User).filter(User.id==id).first()

    if not user_existed:
        raise HTTPException(
            status_code=401,
            detail="User does not exist"
        )
    
    db.close()
    if verify_password(data.password,user_existed.password):
        return{
            "message":"Password verified"
        }
    else:
        raise HTTPException(
            status_code=401,
            detail="Incorrect password"

        )
    
    


@router.post("/reset_verified_password/{id}")
def resetVerifiedPassword(id:int , data:PasswordVerify):
    db = SessionLocal()
    user_existed = db.query(User).filter(User.id==id).first()
    if not user_existed:
        raise HTTPException(
            status_code=401,
            detail="User does not exist"
        )
    
    user_existed.password = hashing_password(data.password)
    db.add(user_existed)
    db.commit()
    
    # sent_password_change_email(user_existed.email)

    db.close()
    return{
        "message":"Password Changed"
    }

    


    
    



