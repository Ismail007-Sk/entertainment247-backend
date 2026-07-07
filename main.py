from fastapi import FastAPI
from database.database import Base,engine
from routes.game_routes import router as game_router
from routes.user_registration_routes import router as auth_router
from routes.login_routes import router as login_router
from routes.protected_routes import router as protected_router
from routes.otp_routes import router as otp_router
from routes.reset_routes import router as reset_router
from routes.refresh_token_routes import router as  refresh_router
from routes.logout_routes import router as logout_router
from routes.password_routes import router as password_router
from routes.upload_routes import router as upload_router
from routes.message_routes import router as messsage_router
from fastapi.middleware.cors import CORSMiddleware

# metadata keeps all data and create_all run it
Base.metadata.create_all(bind=engine)

app = FastAPI()


# when they are on different origins.(Not Tighly couple website, API -> concept used !)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
# The backend gives the green light back to the browser saying,
#  "Yes, I accept these cookies, and it's safe to let the frontend read my response."
    allow_credentials=True,      
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(game_router)

app.include_router(auth_router)

app.include_router(login_router)

app.include_router(protected_router)

app.include_router(otp_router)

app.include_router(reset_router)

app.include_router(refresh_router)

app.include_router(logout_router)

app.include_router(password_router)

app.include_router(upload_router)

app.include_router(messsage_router)