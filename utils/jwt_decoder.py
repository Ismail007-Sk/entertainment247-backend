from jose import jwt ,JWTError
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("secret_key")
ALGORITHM = os.getenv("algorithm")


def verify_jwt_token(token:str):

    # print("token",token)

    try:
        token_data = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return token_data
    
    except JWTError:
        return None

