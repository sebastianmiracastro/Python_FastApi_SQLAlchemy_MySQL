from fastapi import FastAPI;

# IMPORT ENGINE DATABASE

from service.databaseConfig import create_engine

# UTILS TABLES DATABASE

from utils.usersTable import usuarios
from utils.servicesTable import servicios
from utils.subscriptionsTable import suscripciones

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hello World"}