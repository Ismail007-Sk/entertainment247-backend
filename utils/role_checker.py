from fastapi import Depends,HTTPException,status
from utils.authentication_dependency import get_current_user

# def function_name(*args) -> handles multiple argument wihtout declaration.
def check_role(*required_role:str ):

    def checker(user = Depends(get_current_user)):
        if user.role not in required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )
        return user
    
    # FastAPI calls this function. As check_role function return checker, it becomes Depends(checker) 
    # because check_role function was also called as Depends(check_role)
    return checker

    
