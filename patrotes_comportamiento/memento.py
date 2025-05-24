class ConfiguracionUsuario:
    def __init__(self, tema, idioma, volumen):
        self.tema = tema
        self.idioma = idioma
        self.volumen = volumen

    def crear_memento(self):
        return Memento(self.tema, self.idioma, self.volumen)

    def restaurar_memento(self, memento):
        self.tema = memento.tema
        self.idioma = memento.idioma
        self.volumen = memento.volumen

    def __str__(self):
        return f"Tema: {self.tema}, Idioma: {self.idioma}, Volumen: {self.volumen}"

class Memento:
    def __init__(self, tema, idioma, volumen):
        self.tema = tema
        self.idioma = idioma
        self.volumen = volumen

class HistorialConfiguraciones:
    def __init__(self):
        self._historial = []

    def guardar(self, memento):
        self._historial.append(memento)

    def deshacer(self):
        if self._historial:
            return self._historial.pop()
        return None

config = ConfiguracionUsuario("Oscuro", "Español", 70)
historial = HistorialConfiguraciones()

print("[Inicial] ", config)

# Guardar estado inicial
historial.guardar(config.crear_memento())

# Cambios del usuario
config.tema = "Claro"
config.idioma = "Inglés"
config.volumen = 30

print("[Modificado] ", config)

# Deshacer cambios
estado_anterior = historial.deshacer()
if estado_anterior:
    config.restaurar_memento(estado_anterior)

print("[Restaurado] ", config)
