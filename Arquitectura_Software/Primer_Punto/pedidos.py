from fastapi import FastAPI, Request
from pymongo import MongoClient
import os

app = FastAPI()
client = MongoClient(os.environ["MONGO_URL"])
db = client["pedidos_db"]

@app.get("/")
def read_root():
    return {"message": "Servicio de Pedidos funcionando"}

@app.post("/crear")
def crear_pedido(pedido: dict):
    db.pedidos.insert_one(pedido)
    return {"message": "Pedido creado"}
