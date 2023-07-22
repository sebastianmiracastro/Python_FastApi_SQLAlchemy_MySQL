from service.databaseConfig import create_engine

# UTILS TABLES DATABASE

from utils.usersTable import usuarios
from utils.servicesTable import servicios
from utils.subscriptionsTable import suscripciones

from app.main import app

# IMPORT UVICORN
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)