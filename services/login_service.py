from models.user_registration_model import User
from utils.security import verify_password

def login_user(db,data):
    existed_user = db.query(User).filter(User.email==data.email).first()

    if existed_user:
        if verify_password(data.password,existed_user.password):
            return existed_user
        else:
            return None
    else:
        return None
    
    

