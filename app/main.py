from fastapi import FastAPI
from app.api.endpoints import usersEndPoints
from app.api.endpoints import auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(usersEndPoints.router)