class Usuario:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password  # hash de la contraseña
