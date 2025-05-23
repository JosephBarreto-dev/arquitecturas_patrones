from abc import ABC, abstractmethod

class EstadoOrden(ABC):
    @abstractmethod
    def procesar(self):
        pass

    @abstractmethod
    def mostrar_estado(self):
        pass
    
class Pendiente(EstadoOrden):
    def procesar(self):
        print("Pendiente a procesando.")
        return Procesando()
    
    def mostrar_estado(self):
        print("Pendiente...")
    
class Procesando(EstadoOrden):
    def procesar(self):
        print("Procesando a enviado.")
        return Enviado()
    
    def mostrar_estado(self):
        print("Procesando...")
    
class Enviado(EstadoOrden):
    def procesar(self):
        print("Enviado a entregado.")
        return Entregado()
    
    def mostrar_estado(self):
        print("Enviado...")
    
class Entregado(EstadoOrden):
    def procesar(self):
        print("La orden ha sido entregada.")
        return self
    
    def mostrar_estado(self):
        print("Entregado...")
    
class Orden:
    def __init__(self):
        self.estado = Pendiente()
    
    def cambiar_estado(self):
        self.estado = self.estado.procesar()
    
    def mostrar_estado(self):
        return self.estado.mostrar_estado()
    
envio = Orden()

envio.mostrar_estado() # ⏳ Pendiente
envio.cambiar_estado() # 📦 → ⚙️
envio.mostrar_estado() # 🔄 Procesando
envio.cambiar_estado() # ⚙️ → 🚚
envio.mostrar_estado() # 📤 Enviado
envio.cambiar_estado() # 🚚 → ✅
envio.mostrar_estado() # 📬 Entregado
envio.cambiar_estado() # ✅ ya no cambia
