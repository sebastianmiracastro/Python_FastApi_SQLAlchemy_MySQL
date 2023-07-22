import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.auth import create_jwt_token

router = APIRouter()

# RUTA PARA OBTENER TOKEN PARA PETICIONES

@router.get("/token")
def get_token():
    data = {"pruebaToken": "USO_DE_JWT"}
    return {"access": create_jwt_token(data), "token_type": "bearer"}