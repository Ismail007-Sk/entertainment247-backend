from fastapi import Response , HTTPException,APIRouter
from schemas.login_schema import UserLogin
from services import login_service
from database.database import SessionLocal
from utils.jwt_encoder import creat_access_token,create_refresh_token


router = APIRouter()

# Request Body ,Not path parameter , Not Query parameter
@router.post("/login")
def login_user(data:UserLogin,response:Response):
    db = SessionLocal()

    try:
        user_data = login_service.login_user(db,data)

        if not user_data:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )
        # {"sub":data.email "role":data.email} -> can create RBAC based on JWT
        
        # Access Token created
        access_token = creat_access_token({"sub":data.email})
        
        # Refresh Token created
        refresh_token = create_refresh_token({"sub":data.email})


        # Instead of sending JWT to frontend browser, and store to localStorage. 
        # return {
        #     "message": "Successfully logged in.",
        #     "access_token": token,
        #     "token_type": "bearer"
        # }

        # We will store data in reposnse.set_cookie()

        # Store Access Token in HttpOnly Cookie
        response.set_cookie(
            key="access_token",  # We will use this name inside cookies.get() ,while fecthing this from request 
            value=access_token,
            httponly=True,       # Makes the cookie hidden so malicious js code cant access.
            secure=True,        # usecase: True = live website & False = localhost
            samesite="none",      # A gateman that says the browser dont accept request from anonymous website
            max_age= 15 * 60      # 15 minutes
        )

        # Store Refresh Token in HttpOnly Cookie
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=True,      # True in Production (HTTPS)
            samesite="none",
            max_age= 7 * 24 * 60 * 60    # 7 days
        )

        return {
            "message": "Successfully logged in."
        }

    finally:
        # Finally close db after use
        db.close()


    