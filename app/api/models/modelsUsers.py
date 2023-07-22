from pydantic import BaseModel

class User(BaseModel):
    id_Usuario: int
    documento_Usuario: str
    nombreApellido_Usuario: str
    telefono_Usuario: str
    correo_Usuario: str
    suscripciones_Habilitadas: bool

class createUser(BaseModel):
    documento_Usuario: str
    nombreApellido_Usuario: str
    telefono_Usuario: str
    correo_Usuario: str
    suscripciones_Habilitadas: bool