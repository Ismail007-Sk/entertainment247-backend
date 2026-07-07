from fastapi import APIRouter , Response

router = APIRouter()

@router.post("/log_out")
def log_out(response:Response):

    # Delete Access Token
    response.delete_cookie(
        key="access_token"
    )

    # Delete Refresh Token
    response.delete_cookie(
        key="refresh_token"
    )

    return{
        "message":"Logged Out successfully."
    }

