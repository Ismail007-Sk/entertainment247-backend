from sqlalchemy import Column,Integer,String
from database.database import Base


class Product(Base):
    __tablename__ = "gamesTable"

    game_id = Column(Integer, primary_key=True, index=True)
    game_name = Column(String)
    price = Column(Integer)
    story = Column(String)


# class RegisteredUser():
#     __tablename__="RegisteredUser_Data"
#     id:Column(Integer,primary_key=True,index=True)
#     name:Column(String)
#     email:Column(String)
#     password:Column(String)

