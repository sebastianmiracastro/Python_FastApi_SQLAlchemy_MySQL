from sqlalchemy import Table, Column, Integer, String, MetaData

#engine MYSQL

from service.databaseConfig import get_connection

conn = get_connection()

meta = MetaData()

servicios = Table(
    'servicios', meta,
    Column('id_Servicio', Integer, primary_key=True, autoincrement=True),
    Column('nombreServicio', String(100), nullable=False),
    Column('urlApi_Servicio', String(200), nullable=False),
    Column('apiKey_Servicio', String(150), nullable=True)
)

meta.create_all(bind=conn)