from models.user_registration_model import User
from utils.security import hashing_password

# Register User (POST)
def register_user(db,data):
    new_data = User(name=data.name,
                    email=data.email,
                    password=hashing_password(data.password),
                    role="user")
    db.add(new_data)
    db.commit()


# See Users (GET)
def show_users(db):
    return db.query(User).all()

# Update User (PUT)
def update_user(id,db,data):

    user = db.query(User).filter(User.id==id).first()
    if user:
        user.name=data.name
        user.email=data.email
        user.password=data.password

    db.add(user)
    db.commit()    
        

# Edit User (PATCH)
def edit_user(id,db,data):

    user = db.query(User).filter(User.id==id).first()
    if user:
        if data.name is not None:
            user.name=data.name
        if data.email is not None:    
            user.email=data.email
        if data.password is not None:
            user.password=hashing_password(data.password)

    db.add(user)
    db.commit()

# Delete User (DELETE)
def delete_user(id,db):
    user = db.query(User).filter(User.id==id).first()
    if user:
        db.delete(user)
    db.commit()

    
    