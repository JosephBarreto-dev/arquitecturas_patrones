import bcrypt
from models.user import Usuario

class ServicioAutenticacion:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def registrar_usuario(self, username: str, password: str):
        hash_pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        usuario = Usuario(username, hash_pwd)
        self.repositorio.guardar(usuario)
        print(f"Usuario '{username}' registrado.")

    def autenticar(self, username: str, password: str):
        usuario = self.repositorio.obtener_por_username(username)
        if not usuario:
            return False
        return bcrypt.checkpw(password.encode(), usuario.password)
