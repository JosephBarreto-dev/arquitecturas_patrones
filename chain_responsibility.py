from abc import ABC, abstractmethod
import re

class Validador(ABC):
    def __init__(self):
        self.siguiente = None
        
    def establecer_siguiente(self, validador):
        self.siguiente = validador
        return validador
    
    def manejar(self, datos):
        if self.validar(datos):
            if self.siguiente:
                return self.siguiente.manejar(datos)
            return True
        return False
    
    @abstractmethod
    def validar(self, datos):
        pass
    
class ValidarNombre(Validador):
    def validar(self, datos):
        if not datos.get("nombre"):
            print("Error: El nombre está vacío.")
            return False
        return True
    
class ValidarCorreo(Validador):
    def validar(self, datos):
        correo = datos.get('correo', '')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            print(f"Correo inválido: {correo}")
            return False
        return True
    
class ValidarContraseña(Validador):
    def validar(self, datos):
        contra = datos.get('contraseña', '')
        if len(contra) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
            return False
        return True
    
# Ejemplo de uso
# Configurar cadena de validadores
validador = ValidarNombre()
validador.establecer_siguiente(ValidarCorreo()).establecer_siguiente(ValidarContraseña())

# Formulario de ejemplo
formulario = {
    "nombre": "Joseph",
    "correo": "josephcorreo.com",
    "contraseña": "secreta1234"
}

if validador.manejar(formulario):
    print("Formulario válido. Enviando datos...")
else:
    print("Formulario inválido.")
