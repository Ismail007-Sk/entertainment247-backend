from pydantic import BaseModel,EmailStr

# As only two types of user we are using -> admin ,normal user so role in this scheme not needed
# Admin will be created manually and rest will by default users, 
# For multiple types of users(nurse , patient, doctor) role:str can be used 
class RegisterUser(BaseModel):
    name:str
    email:EmailStr
    password:str

  
# Here role used as so that admin could later promot normal user to admin.
class PatchUser(BaseModel):
    name:str | None = None
    email:EmailStr | None = None
    password:str | None = None
    role:str | None = None


