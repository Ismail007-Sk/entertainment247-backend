# Role-Based Access Control (RBAC)

RBAC (Role-Based Access Control) can be implemented in two ways.

---

# 1. Manual RBAC Checking (Database Role Checking)

In this method, every time a user accesses an admin feature, the backend retrieves the user from the database and checks the user's role.

```python
current_user = db.query(User).filter(User.id == user_id).first()

if current_user.role != "admin":
    raise HTTPException(403)
```

### Flow

* Retrieve the user from the database.
* Check whether `current_user.role == "admin"` or not.
* If not, return **403 Permission Denied**.

### Example
get_current_user() checks authentic jwt by decoding it. While using Manual RBAC method
this function  get_current_user() should return { "sub":"absc@gmal.com", "exp":"anyduration time" } 

But why can modify this function a little so it could ( return user data + do athentication )
If we do this it will minimize manual codding a little.
And we can use this Code.

```python
from fastapi import Depends, HTTPException, status
from auth import get_current_user

def require_role(required_role: str):

    def role_checker(user=Depends(get_current_user)):

        if user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )

        return user

    return role_checker
```

### Advantages

* Every request checks the latest user role from the database.
* If an admin is demoted to a normal user, the change takes effect immediately.
* Very secure because it always uses the latest database information.

### Disadvantages

* Performs one database query on every protected request.
* If written manually for every endpoint, the same role-checking code gets repeated.

> The repeated code can be reduced by creating a common dependency.

---

# Normal JWT Authentication (Role Not Included in JWT)

Here, the JWT is only used for authentication. 
But we can modify it so it could give user data as well, then there will be no need to create another service code to fecth user data!

```python
@router.get("/game_info")
def get_all_games(user=Depends(get_current_user)):
    db = SessionLocal()
    return game_service.get_all_games(db)
```

`get_current_user()` only verifies:

* JWT authenticity
* JWT expiration
* User identity

---

# 2. RBAC Using JWT Role

In this method, the user's role is also stored inside the JWT token.

Just like `get_current_user()` checks the authenticity of the JWT, another dependency can be created to check the user's role.

## Role Dependency

```python
from fastapi import Depends, HTTPException, status
from auth import get_current_user

def require_role(required_role: str):

    def role_checker(user=Depends(get_current_user)):

        if user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )

        return user

    return role_checker
```

get_current_user() checks authentic jwt by decoding it. While using RBAC JWT method
this function  get_current_user() should return { "sub":"absc@gmal.com", "role":"anyrole", "exp":"anyduration time" } 

## Usage

```python
from dependencies.role_checker import require_role

@router.post("/add_game")
def add_game(
    game: GameCreate,
    user=Depends(require_role("admin"))
):
    ...
```

### Advantages

* Just call the dependency.
* No need to retrieve the user from the database every time just to check the role.
* Faster because it reduces database queries.
* Less repeated code.

---

# Major Drawback

Suppose a user is an admin and already has a JWT containing:

```text
role = admin
```

Later, the admin is demoted to a normal user in the database.

The problem is that the old JWT still says **admin**, so the user can continue using admin features until the JWT expires or a new token is issued.

Since this method does not check the database for the latest role, any role changes will not take effect immediately.

---

# My Choice

I prefer **Option 1 (Database RBAC)** because:

* It always checks the latest user role from the database.
* If a user's role changes, the change takes effect immediately.
* It is more secure.

The only downside is one database query on every protected request, which is acceptable for my project.
