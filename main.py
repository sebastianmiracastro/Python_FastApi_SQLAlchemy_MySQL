# UTILS TABLES DATABASE

from utils.usersTable import usuarios
from utils.servicesTable import servicios
from utils.subscriptionsTable import suscripciones

from app.main import app

# IMPORT UVICORN
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)