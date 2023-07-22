
# IMPORT ROUTERS

from fastapi import APIRouter, HTTPException, Depends

# IMPORT SQLALCHEMY METHODS

from sqlalchemy import exc

# IMPORT MODELS

from app.api.models.modelsUsers import User, createUser

# IMPORT DB CONNECTION

from service.databaseConfig import get_connection

from utils.usersTable import usuarios

# JWT CORE AUTH

from app.core.auth import get_current_user

router = APIRouter()

# OPERATIONAL PATHS FIR CRUD USERS

@router.post("/users/createUserV1/", response_model=User)
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
                documentoUsuario= user_create.documento_Usuario,
                nombre_ApellidoUsuario= user_create.nombreApellido_Usuario,
                telefonoUsuario= user_create.telefono_Usuario,
                correoUsuario= user_create.correo_Usuario,
                suscripcionesHabilitadas= user_create.suscripciones_Habilitadas
            )
        )

        user_id = result.lastrowid
        
        # conn.close()

        return {
            "id_Usuario": user_id,
            "documentoUsuario": user_create.documento,
            "nombre_ApellidoUsuario": user_create.nombre_apellido,
            "telefonoUsuario": user_create.telefono,
            "correoUsuario": user_create.correo,
            "suscripcionesHabilitadas": user_create.suscripciones_habilitadas
        }

    except exc.OperationalError as op_err:
        raise HTTPException(status_code=500, detail=f"Error operacional en la base de datos: {str(op_err)}")
    except exc.IntegrityError as int_err:
        raise HTTPException(status_code=500, detail=f"Error de integridad de la base de datos: {str(int_err)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error interno del servidor! - - {e}')


@router.get("/users/getUserV2/{documentoUsuario}", response_model=User)
async def get_user_by_document(documentoUsuario: str, user: dict = Depends(get_current_user)):
    conn = get_connection()

    if user is None:
        raise HTTPException(status_code=401, detail='Token inválido')

    try:
        result = conn.execute(
            usuarios.select().where(usuarios.c.documentoUsuario == documentoUsuario)
        ).fetchone()
        
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
            
        # conn.close()

        return userData

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error! - {str(e)}")
