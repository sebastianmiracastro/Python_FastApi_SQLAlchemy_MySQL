from sqlalchemy import Table, Column, Integer, String, MetaData, Boolean

#engine MYSQL

from service.databaseConfig import get_connection

conn = get_connection()

meta = MetaData()

usuarios = Table(
    'usuarios', meta,
    Column('id_Usuario', Integer, primary_key=True, autoincrement=True),
    Column('documentoUsuario', String(25), nullable=False),
    Column('nombre_ApellidoUsuario', String(100), nullable=False),
    Column('telefonoUsuario', String(100), nullable=False),
    Column('correoUsuario', String(100), nullable=False),
    Column('suscripcionesHabilitadas', Boolean)
)

meta.create_all(bind=conn)