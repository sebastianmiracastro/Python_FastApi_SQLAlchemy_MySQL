from sqlalchemy import Table, Column, Integer, DateTime, ForeignKey, MetaData, Boolean

#engine MYSQL

from service.databaseConfig import get_connection

conn = get_connection()

# FOREIGN KEY CONNECTIONS

from utils.usersTable import usuarios
from utils.servicesTable import servicios

meta = MetaData()

suscripciones = Table(
    'suscripciones', meta,
    Column('id_Suscripcion', Integer, primary_key=True, autoincrement=True),
    Column('id_Usuario_suscripcion',Integer , ForeignKey(usuarios.c.id_Usuario) ,nullable=False),
    Column('id_servicio_suscripcion', Integer, ForeignKey(servicios.c.id_Servicio), nullable=False),
    Column('fecha_suscripcion', DateTime, nullable=False),
    Column('activa_suscripcion', Boolean),
    Column('fecha_desuscripcion', DateTime, nullable=True)
)

meta.create_all(bind=conn)