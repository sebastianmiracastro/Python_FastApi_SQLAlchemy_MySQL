
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

def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            userInnDB, passWord, host, port, database
        )
    )

if __name__ == '__main__':
    try:
        # GET CONNECTION OBJECT
        engine = get_connection()
    except Exception as ex:
        print(f"CONNECTION_NOT_AVAILABLE -- ERROR : {ex}")