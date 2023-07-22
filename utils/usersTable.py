from sqlalchemy import Table, Column, Integer, String, MetaData

#engine MYSQL

from service.databaseConfig import get_connection

conn = get_connection();

meta = MetaData()

usuarios = Table(
    'usuarios', meta,
    Column('id_Usuario', Integer, primary_key=True, autoincrement=True)
)

meta.create_all(bind=conn)