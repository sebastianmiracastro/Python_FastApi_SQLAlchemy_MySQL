
# IMPORT ROUTERS

from fastapi import APIRouter, HTTPException, Depends

# IMPORT MODELS

from app.api.models.modelsUsers import User, createUser

# IMPORT DB CONNECTION

from service.databaseConfig import get_connection

from utils.usersTable import usuarios

# JWT CORE AUTH

from app.core.auth import get_current_user

router = APIRouter()

# OPERATIONAL PATHS FIR CRUD USERS

@router.post("/users/createUser/", response_model=User)
def create_user(user_create: createUser, current_user: dict = Depends(get_current_user)):
    conn = get_connection()

    if current_user is None:
        raise HTTPException(status_code=401, detail="Token Inválido")

    try:
        existing_user = conn.execute(
            usuarios.select().where(usuarios.c.documentoUsuario == user_create.documento_Usuario)
        ).fetchone()

        if existing_user:
            raise HTTPException(status_code=400, detail="El usuario ya existe!")

        result = conn.execute(
            usuarios.insert().values(
                documento_Usuario= user_create.documento_Usuario,
                nombreApellido_Usuario= user_create.nombreApellido_Usuario,
                telefono_Usuario= user_create.telefono_Usuario,
                correo_Usuario= user_create.correo_Usuario,
                suscripciones_Habilitadas= user_create.suscripciones_Habilitadas
            )
        )

        user_id = result.lastrowid
        
        conn.close()

        return {
            "id_Usuario": user_id,
            "documentoUsuario": user_create.documento,
            "nombre_ApellidoUsuario": user_create.nombre_apellido,
            "telefonoUsuario": user_create.telefono,
            "correoUsuario": user_create.correo,
            "suscripcionesHabilitadas": user_create.suscripciones_habilitadas
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal server error!')


@router.get("/users/getUserV1/{documentoUsuario}", response_model=User)
async def get_user_by_document(documentoUsuario: str, user: dict = Depends(get_current_user)):
    conn = get_connection()

    if user is None:
        raise HTTPException(status_code=401, detail='Token inválido')

    try:
        query = "SELECT * FROM usuarios WHERE documentoUsuario=:documentoUsuario"
        result = conn.execute(query, {"documentoUsuario": documentoUsuario}).fetchone()
        
        if result is None:
            raise HTTPException(status_code=404, detail="Users not found!")
            
        userData = User(
            id_Usuario=result["id_Usuario"],
            documento_Usuario=result["documentoUsuario"],
            nombreApellido_Usuario=result["nombre_ApellidoUsuario"],
            telefono_Usuario=result["telefonoUsuario"],
            correo_Usuario=result["correoUsuario"],
            suscripciones_Habilitadas=result["suscripcionesHabilitadas"]
        )
            
        conn.close()

        return userData

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error!")
