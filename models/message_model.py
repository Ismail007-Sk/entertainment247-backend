from database.database import Base
from sqlalchemy import Column, String, Integer ,DateTime

class User_Message(Base):
    __tablename__ = "message_table"

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer)
    subject = Column(String)
    message = Column(String)
    status = Column(String,default="open")
    created_at = Column(DateTime(timezone=True))
    solved_at = Column(DateTime(timezone=True))
