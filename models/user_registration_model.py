from sqlalchemy import Column,String,Integer
from database.database import Base

class User(Base):
    __tablename__ = "usertable"
    
    id = Column(Integer ,primary_key=True ,index=True)
    name = Column(String)
    email = Column(String,unique=True)
    password = Column(String)
    role = Column(String,default="user")


