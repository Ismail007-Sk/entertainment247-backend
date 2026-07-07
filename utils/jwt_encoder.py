from jose import jwt 
from datetime import datetime ,timedelta ,timezone

import os 
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("secret_key")
ALGORITHM = os.getenv("algorithm")

# Access Token (expire time = 15 minutes)
def creat_access_token(data:dict):
    playload = data.copy() #shallow copy
    expire_time = datetime.now(timezone.utc)+timedelta(minutes=15)
    playload.update({"exp":expire_time}) #updating dictionary

    access_token = jwt.encode(playload,SECRET_KEY,algorithm=ALGORITHM)

    return access_token



# Refresh Token (expire time = 7 days)
def create_refresh_token(data:dict):
    playload = data.copy()
    expire_time = datetime.now(timezone.utc)+timedelta(days=7)
    playload.update({"exp":expire_time})

    refresh_token = jwt.encode(playload,SECRET_KEY,algorithm=ALGORITHM)

    return refresh_token
