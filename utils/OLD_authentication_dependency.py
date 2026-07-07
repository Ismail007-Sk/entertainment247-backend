# OLD method using HTTPBearer, takes jwt token From browser localStorage and verifies it! 
# Another authentication_dependency.py will be created to handle cookie based authentication system.



from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.jwt_decoder import verify_jwt_token
from models.user_registration_model import User
from database.database import SessionLocal
from fastapi import HTTPException



# HTTPBearer work
# incomming Authorization: Bearer eyJhbGciOi...
# Splits it
# Returns:
#     authentication.scheme = "Bearer"
#     authentication.credentials = "eyJhbGciOi..."




# Create Bearer authentication scheme
auth_scheme = HTTPBearer()

# HTTPAuthorizationCredentials prepares the `auth_data` variable,
# similar to a type annotation like `value: int`. 

# It's called Authentication = "Who are you?"
# Verifies the JWT token and returns the authenticated user.
def get_current_user(auth_data: HTTPAuthorizationCredentials = Depends(auth_scheme)):

    if not auth_data.credentials:
        raise HTTPException(
            status_code=401,
            detail="Token Missing"
        )
    # Print the received token
    # print("Token Received:", credentials.credentials)

    decoded_token = verify_jwt_token(auth_data.credentials)

    if not decoded_token:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    # return decoded_token 
    # Upto this,  get_current_user will return { "sub":"absc@gmal.com", "exp":"anyduration time" } 
    # Upto this, get_current_user only check authenticity of JWT token.

    # Modification
    email = decoded_token.get("sub") # decoded_token returns dictionary so .get()

    db = SessionLocal()

    current_user_data = db.query(User).filter(User.email==email).first()

    db.close()

    if current_user_data is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    
    return current_user_data


# retuns   
#   {
#     "id": data,
#     "password": "data",
#     "role": "data",
#     "name": "data",
#     "email": "data"
#   }



