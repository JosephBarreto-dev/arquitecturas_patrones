from abc import ABC, abstractmethod

# Todo usuario que quiera enterarse de descuentos, debe tener un método para ser notificado = abstractmethod
class Usuario(ABC):
    @abstractmethod
    def actualizar(self, producto):
        pass
        

class UsuarioConcreto(Usuario):
    def __init__(self, nombre):
        self.nombre = nombre
        
    def actualizar(self, producto):
        print(f'Hola {self.nombre}, el producto {producto.nombre} ahora esta en descuento por {producto.descuento}%')
    
class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.descuento = 0
        self.suscriptores = []
        
    def suscribir(self, usuario):
        self.suscriptores.append(usuario)
        
    def desuscribir(self, usuario):
        self.suscriptores.remove(usuario)
        
    def notificar(self):
        for suscriptor in self.suscriptores:
            suscriptor.actualizar(self)
    
    def aplicar_descuento(self, descuento):
        # Cambia el valor del descuento del producto.
        self.descuento = descuento
        print(f'El producto {self.nombre} ahora tiene un descuento de {self.descuento}%')
        self.notificar()
        
# Ejemplo de uso
producto = Producto('Zapatos')

usuario1 = UsuarioConcreto('Juan')
usuario2 = UsuarioConcreto('Maria')

producto.suscribir(usuario1)
producto.suscribir(usuario2)

producto.aplicar_descuento(20)

producto.desuscribir(usuario2)

producto.aplicar_descuento(30)