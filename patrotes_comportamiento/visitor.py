from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def aceptar(self, visitante):
        pass

class Alimento(Producto):
    def aceptar(self, visitante):
        return visitante.visitar_alimento(self)

class Tecnologia(Producto):
    def aceptar(self, visitante):
        return visitante.visitar_tecnologia(self)

class Servicio(Producto):
    def aceptar(self, visitante):
        return visitante.visitar_servicio(self)

class VisitanteImpuesto(ABC):
    @abstractmethod
    def visitar_alimento(self, alimento):
        pass

    @abstractmethod
    def visitar_tecnologia(self, tecnologia):
        pass

    @abstractmethod
    def visitar_servicio(self, servicio):
        pass

class CalculadoraImpuesto(VisitanteImpuesto):
    def visitar_alimento(self, alimento):
        return alimento.precio * 0.05  # 5% impuesto

    def visitar_tecnologia(self, tecnologia):
        return tecnologia.precio * 0.18  # 18% impuesto

    def visitar_servicio(self, servicio):
        return servicio.precio * 0.12  # 12% impuesto

productos = [
    Alimento("Pan", 100),
    Tecnologia("Laptop", 2000),
    Servicio("Consultoría", 500)
]

visitante = CalculadoraImpuesto()

for producto in productos:
    impuesto = producto.aceptar(visitante)
    print(f"Impuesto de {producto.nombre}: ${impuesto:.2f}")
