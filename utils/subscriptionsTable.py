from sqlalchemy import Table, Column, Integer, DateTime, ForeignKey, MetaData, Boolean

#engine MYSQL

from service.databaseConfig import get_connection

conn = get_connection()

meta = MetaData()

suscripciones = Table(
    'suscripciones', meta,
    Column('id_Suscripcion', Integer, primary_key=True, autoincrement=True),
    Column('id_Usuario_suscripcion',Integer , ForeignKey('usuarios.id_Usuario') ,nullable=False),
    Column('id_servicio_suscripcion', Integer, ForeignKey('servicios.id_Servicio'), nullable=False),
    Column('fecha_suscripcion', DateTime, nullable=False),
    Column('activa_suscripcion', Boolean),
    Column('fecha_desuscripcion', DateTime, nullable=True)
)

meta.create_all(bind=conn)