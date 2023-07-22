
# IMPORT SQLALCHEMY LIBRARY - CREATE_ENGINE METHOD

from sqlalchemy import create_engine

# CONTROLS .ENV FILE

import os
from dotenv import load_dotenv

load_dotenv()

# DATABASE CREDENTIALS

userInnDB = os.getenv('USER_DATABASE_PY')
passWord = ""
host = os.getenv('HOST_DATABASE_PY')
port = 3306
database = os.getenv('DATABASE_NAME_PY')

# PYTHON FUNCTIONS TO CONNECT MYSQL DATABASE

# ... (código existente)

def create_engine_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            userInnDB, passWord, host, port, database
        )
    )

def get_connection():
    engine = create_engine_connection()
    connection = engine.connect()
    return connection

if __name__ == '__main__':
    try:
        # GET CONNECTION OBJECT
        engine = create_engine_connection()
        connection = engine.connect()
        print("Connection successful!")
        connection.close()
    except Exception as ex:
        print(f"CONNECTION_NOT_AVAILABLE -- ERROR : {ex}")
