from fastapi import APIRouter
from database.database import SessionLocal
from schemas.user_registraion_schema import PatchUser,RegisterUser
from services import user_registration_service
from services.email_service import welcome_email
router = APIRouter()


# POST
@router.post("/signup")
def register_user(data:RegisterUser):
    db = SessionLocal()
    user_registration_service.register_user(db,data)
    # welcome_email(data.name , data.email ,"user")

    return {"message":"new user registered successfully"}


# GET 
@router.get("/signup")
def show_users():
    db = SessionLocal()
    return user_registration_service.show_users(db)


# PUT
@router.put("/signup/{id}")
def update_user(id:int,data:RegisterUser):
    db = SessionLocal()
    user_registration_service.update_user(id,db,data)
    return {"message":"user updated successfully"}


# PATCH
@router.patch("/signup/{id}")
def edit_user(id:int,data:PatchUser):
    db = SessionLocal()
    user_registration_service.edit_user(id,db,data)
    return {"message":"user edited successfully"}


# DELETE
@router.delete("/signup/{id}")
def delete_user(id:int):
    db = SessionLocal()
    user_registration_service.delete_user(id,db)
    return {"message":"user deleted successfully"}

