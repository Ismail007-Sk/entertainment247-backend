from passlib.context import CryptContext

# Creating an instance of the CryptContext class.
# Choosing the "bcrypt" algorithm (others like argon2 are also available).
# deprecated="auto" makes hashing flexible: if you change algorithms in the future,
# passlib automatically handles updating old user passwords during login.
pwd_context = CryptContext(schemes=["bcrypt"],deprecated=["auto"])


# Hashing password , ISMAIL -> #$#d3$
def hashing_password(password:str):
    return pwd_context.hash(password)

# Verifying a password during login
def verify_password(plain_password:str,hash_password:str):
    return pwd_context.verify(plain_password,hash_password)

