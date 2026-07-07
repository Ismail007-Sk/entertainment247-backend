from services.message_service import all_user_message, create_message, problem_resloved
from database.database import SessionLocal
from schemas.message_schema import Message ,Resolve_Message
from fastapi import APIRouter,HTTPException,Depends
from utils import authentication_dependency,role_checker
from models.user_registration_model import User


router = APIRouter()


# User Posting message
@router.post("/user_message")
def Describe_Message(data:Message, user=Depends(authentication_dependency.get_current_user)):
    db=SessionLocal()
     # If user exixted in main table
    existed_user = db.query(User).filter(User.id==user.id).first()

    if not existed_user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    create_message(db,data,user.id)

    return{
        "message":"User issue submitted."
    }

# Get All User issues
@router.get("/all_user_issue")
def All_message(user=Depends(role_checker.check_role("admin"))):
    db=SessionLocal()
    return all_user_message(db)



# Marke Resolved issues ,
@router.post("/mark_resolved_issue/{issue_id}")
def Resolve_issue(issue_id:int, data:Resolve_Message, user= Depends(role_checker.check_role("admin"))):
    db=SessionLocal()
     # Only those user can enter issue in message_table who belongs to main User table, 
     # so dont need to check user_exixts again

    problem_resloved(db,data,issue_id)

    return {
        "message": "Issue marked as resolved."
    }









