from fastapi import FastAPI;

# UTILS TABLES DATABASE

from utils.usersTable import usuarios

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hello World"}