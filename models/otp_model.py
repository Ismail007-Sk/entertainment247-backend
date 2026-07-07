from sqlalchemy import Column, String, Integer, DateTime
from database.database import Base

class OTP(Base):
    __tablename__ = "otp_table"

    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,nullable=False,index=True,unique=True) 
    otp = Column(String(6),nullable=False)
    created_at = Column(DateTime(timezone=True),nullable=False)
    expires_at = Column(DateTime(timezone=True),nullable=False)
   
    


# index -> to search email efficiently

# unique = True -> Allows only one record per email.
#   A new OTP replaces the previous OTP for the same email,
#   keeping the table clean and avoiding duplicate records.