from fastapi import FastAPI, Request
from pymongo import MongoClient
import os

app = FastAPI()
client = MongoClient(os.environ["MONGO_URL"])
db = client["productos_db"]

@app.get("/")
def read_root():
    return {"message": "Servicio de prouctos funcionando"}

@app.post("/nuevo")
def nuevo_producto(producto: dict):
    db.productos.insert_one(producto)
    return {"message": "producto agregado"}
