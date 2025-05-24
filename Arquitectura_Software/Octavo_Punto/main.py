from data.user_repository import RepositorioUsuario
from business.auth_service import ServicioAutenticacion

repositorio = RepositorioUsuario()
auth = ServicioAutenticacion(repositorio)

# Registrar usuarios
auth.registrar_usuario("nicolas", "gustambo123")

# Autenticación
usuario = input("Usuario: ")
clave = input("Contraseña: ")

if auth.autenticar(usuario, clave):
    print("Acceso permitido")
else:
    print("Acceso denegado")
