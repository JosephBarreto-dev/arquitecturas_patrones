from abc import ABC, abstractmethod

class ServicioPago(ABC):
    @abstractmethod
    def procesar_pago(self, orden): pass
