from fastapi import APIRouter, HTTPException, Response, Request
from utils.jwt_encoder import creat_access_token
from utils.jwt_decoder import verify_jwt_token

router = APIRouter()

@router.post("/refresh_token")
def Refresh_Token(response:Response,request:Request):
    
    # fecth the refresh_token inside request comming from browser httpOnly cookie
    refresh_toke = request.cookies.get("refresh_token")
    
    if not refresh_toke:
        raise HTTPException(
            status_code=401,
            detail="Refresh Token missing"
        ) 
    
    decoded_refresh_token = verify_jwt_token(refresh_toke)

    if not decoded_refresh_token:
        raise HTTPException(
            status_code=401,
            detail="Expired or Invalid Refresh Token"
        )
    
    email = decoded_refresh_token.get("sub")
    
    # Creating new Access Token
    new_access_token = creat_access_token({"sub":email})

    # storing new access token in HttpOnly Cookie
    response.set_cookie(
        key="access_token",
        value=new_access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=15*60
    )
    
    return {
        "message": "Access token refreshed successfully."
    }
