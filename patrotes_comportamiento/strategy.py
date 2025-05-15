from abc import ABC, abstractmethod
from datetime import datetime

class Producto:
    def __init__(self, nombre, precio, popularidad, fecha):
        self.nombre = nombre
        self.precio = precio
        self.popularidad = popularidad
        self.fecha = fecha
        
    def __str__(self):
        return f"{self.nombre} | ${self.precio} | Popularidad: {self.popularidad} | Fecha: {self.fecha.date()}"


class EstrategiaOrdenamiento(ABC):
    @abstractmethod
    def ordenar(self, productos):
        pass
    
class OrdenarPrecio(EstrategiaOrdenamiento):
    def ordenar(self, productos):
        return sorted(productos, key=lambda p: p.precio)
    
class OrdenarPopularidad(EstrategiaOrdenamiento):
    def ordenar(self, productos):
        return sorted(productos, key=lambda p: p.popularidad, reverse=True)
    
class OrdenarFecha(EstrategiaOrdenamiento):
    def ordenar(self, productos):
        return sorted(productos, key=lambda p: p.fecha)
    
class GestorProductos:
    def __init__(self, productos, estrategia: EstrategiaOrdenamiento):
        self.productos = productos
        self.estrategia = estrategia
        
    def cambiar_estrategia(self, nueva_estrategia: EstrategiaOrdenamiento):
        self.estrategia = nueva_estrategia
        
    def mostrar_productos_ordenados(self):
        productos_ordenados = self.estrategia.ordenar(self.productos)
        for producto in productos_ordenados:
            print(producto)
            
# Ejemplo de uso
productos = [
    Producto("Laptop", 1500, 90, datetime(2024, 3, 15)),
    Producto("Mouse", 25, 70, datetime(2025, 1, 10)),
    Producto("Monitor", 300, 85, datetime(2023, 11, 5)),
    Producto("Teclado", 100, 80, datetime(2025, 2, 2))
]

gestor = GestorProductos(productos, OrdenarPrecio())
print("Ordenando por precio:")
gestor.mostrar_productos_ordenados()

print("\nCambiando estrategia a popularidad:")
gestor.cambiar_estrategia(OrdenarPopularidad())
gestor.mostrar_productos_ordenados()

print("\nCambiando estrategia a fecha:")
gestor.cambiar_estrategia(OrdenarFecha())
gestor.mostrar_productos_ordenados()