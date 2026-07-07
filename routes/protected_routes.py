from fastapi import Depends,APIRouter 
from utils.authentication_dependency import get_current_user

router = APIRouter()

####################################################################
#
# helper_function -> Can be a (function, class,object)
#
# Dependency Injection (Depends) means instead of calling a helper function 
# inside your code, you put it in the parameters. FastAPI runs it automatically 
# and hands you the result.
#
# ---->Normal method
# def function():
#   helper_function() 
#
# ---->Dependency Injection
# def function(user=Depends(helper_function)):
#   no need to call inside
#   
# Benefit-> Reusable, Clean, Less duplicate code, Modular, Easy testing, Automatic execution
# UseCase-> Authentication, Database connection, Permission checks, Rate limiting
#
####################################################################



# "Dependency functions can have parameters, but FastAPI automatically provides 
# those parameters from the request or from other dependencies.(such as Header, Query, Path, Cookie, or even other dependencies)"
@router.get("/profile")
def profile(user=Depends(get_current_user)):
    
    return {
        "message": "Welcome",
        "user": user
    }
