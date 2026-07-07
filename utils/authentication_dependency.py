# FastAPI handles (path,query) parameters and JSON bodies natively via Pydantic models, 
# But you must use the Request object to access low-level network 
# And browser data like client IPs, raw headers, and HTTP cookies.

from fastapi import Request ,HTTPException
from utils.jwt_decoder import verify_jwt_token

from models.user_registration_model import User
from database.database import SessionLocal

def get_current_user(request:Request):

    # fecth the access_token inside request comming from browser httpOnly cookie
    access_token = request.cookies.get("access_token")

    if not access_token:
        raise HTTPException(
            status_code=401,
            detail="Access Token Missing"
        )
    # Verify access_token JWT
    decoded_access_token = verify_jwt_token(access_token)

    if not decoded_access_token:
        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Access Token"
        )
    
    # Modifiation-> Below code makes get_current_user function ready for (jwt authentication+RBAC)
    
    # getting email from this dictionary using "sub" key
    email = decoded_access_token.get("sub") 

    db = SessionLocal()
    current_user = db.query(User).filter(User.email==email).first()
    db.close()

    if current_user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found!"
        )

    return current_user 

    
    


