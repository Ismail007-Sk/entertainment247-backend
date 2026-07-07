from fastapi import HTTPException

from models.message_model import User_Message
from datetime import datetime , timezone 


def create_message(db,data,user_id):

    new_message = User_Message(    
                user_id = user_id,
                subject = data.subject,
                message = data.description,
                status = "open",
                created_at = datetime.now(timezone.utc),
                solved_at = " ")
    db.add(new_message)
    db.commit()
    db.close()


def all_user_message(db):
    return  db.query(User_Message).all()


# Marking as Close after solving the problem
def problem_resloved(db,data,issue_id):

    user_with_problem = db.query(User_Message).filter(User_Message.id==issue_id).first()

    if not user_with_problem:
        raise HTTPException(
            status_code=404,
            detail="User with Issue not found."
        )


    user_with_problem.status = data.status
    user_with_problem.solved_at = datetime.now(timezone.utc)

    db.commit()