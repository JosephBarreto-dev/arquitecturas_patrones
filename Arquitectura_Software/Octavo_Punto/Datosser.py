from models.user import Usuario

class RepositorioUsuario:
    def __init__(self):
        self.usuarios = {}

    def guardar(self, usuario: Usuario):
        self.usuarios[usuario.username] = usuario

    def obtener_por_username(self, username: str):
        return self.usuarios.get(username)
