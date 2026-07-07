from models.otp_model import OTP
from datetime import datetime,timedelta,timezone
import secrets # To generate different OTP or password combination
# It's more secure than random function in python.

OTP_EXPIRE_TIME = 5


# Generate OTP
def generate_otp()->str:   # -> this set the return type ,if -> int then return type becomes integer
    return f"{secrets.randbelow(900000)+100000}"   # ensures 6 digit otp



# Save OTP
def save_otp(db,email:str,new_otp:str):

    email_existed = db.query(OTP).filter(OTP.email==email).first()

    current_time = datetime.now(timezone.utc)
    expire_time = datetime.now(timezone.utc) + timedelta(minutes=OTP_EXPIRE_TIME)
    # if email already existed in OTP model/otp_table
    if email_existed:
        email_existed.otp=new_otp
        email_existed.created_at = current_time
        email_existed.expires_at = expire_time

        db.add(email_existed)

    else: # email not exists in otp_table

        new_data = OTP(
            email = email,
            otp = new_otp,
            created_at = current_time,
            expires_at = expire_time
            ) 
        db.add(new_data)

    db.commit()



# Verify OTP
def verify_otp(db,email:str,otp:str)->bool:
    
    email_existed = db.query(OTP).filter(OTP.email==email,OTP.otp==otp).first()

    if not email_existed:
        return False
    if email_existed.expires_at < datetime.now(timezone.utc):
        return False

    return True    
 

# Delete OTP
def delete_otp(db , email:str):
    email_existed = db.query(OTP).filter(OTP.email==email).first()

    if email_existed:
        db.delete(email_existed)

    db.commit()