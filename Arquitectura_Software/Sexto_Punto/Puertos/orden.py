from abc import ABC, abstractmethod

class RepositorioOrden(ABC):
    @abstractmethod
    def guardar(self, orden): pass
