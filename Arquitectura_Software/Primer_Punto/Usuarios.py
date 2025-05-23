from fastapi import FastAPI, Request
from pymongo import MongoClient
import os

app = FastAPI()
client = MongoClient(os.environ["MONGO_URL"])
db = client["usuarios_db"]

@app.get("/")
def read_root():
    return {"message": "Servicio de Usuarios funcionando"}

@app.post("/register")
def register_user(user: dict):
    db.usuarios.insert_one(user)
    return {"message": "Usuario registrado"}
