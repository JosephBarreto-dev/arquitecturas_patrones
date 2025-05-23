from ports.repositorio_orden import RepositorioOrden
from pymongo import MongoClient

class MongoRepositorioOrden(RepositorioOrden):
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["ecommerce"]
        self.collection = self.db["rdenes"]

    def guardar(self, orden):
        data = {
            "productos": orden.productos,
            "total": orden.total,
            "pagada": orden.pagada
        }
        self.collection.insert_one(data)
