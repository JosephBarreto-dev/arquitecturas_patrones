from abc import ABC, abstractmethod

class ChatRoomMediator(ABC):
    @abstractmethod
    def enviar_mensaje(self, mensaje, emisor):
        pass

class ChatRoom(ChatRoomMediator):
    def __init__(self):
        self.usuarios = []

    def registrar(self, usuario):
        self.usuarios.append(usuario)

    def enviar_mensaje(self, mensaje, emisor):
        for usuario in self.usuarios:
            if usuario != emisor:
                usuario.recibir(mensaje, emisor)

class Usuario:
    def __init__(self, nombre, sala_chat):
        self.nombre = nombre
        self.sala_chat = sala_chat
        self.sala_chat.registrar(self)

    def enviar(self, mensaje):
        print(f"{self.nombre} envía: {mensaje}")
        self.sala_chat.enviar_mensaje(mensaje, self)

    def recibir(self, mensaje, emisor):
        print(f"{self.nombre} recibe de {emisor.nombre}: {mensaje}")

sala = ChatRoom()

joseph = Usuario("Joseph", sala)
ana = Usuario("Ana", sala)
luis = Usuario("Luis", sala)

joseph.enviar("Hola a todos 👋")
ana.enviar("¡Hola Joseph!")
