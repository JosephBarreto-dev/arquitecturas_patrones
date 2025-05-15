from abc import ABC, abstractmethod

class EditorTexto:
    def __init__(self):
        self.contenido = ""
        
    def escribir(self, texto):
        self.contenido += texto
        
    def borrar(self, longitud):
        self.contenido = self.contenido[:-longitud]
        
    def mostrar(self):
        print('Contenido actual: ', self.contenido)

class Command(ABC):
    @abstractmethod
    def ejecutar(self):
        pass
    
    def deshacer(self):
        pass
    
class EscribirTextoCommand(Command):
    def __init__(self, editor, texto):
        self.editor = editor
        self.texto = texto
        
    def ejecutar(self):
        self.editor.escribir(self.texto)
        
    def deshacer(self):
        self.editor.borrar(len(self.texto))
    
class AdminComandos:
    def __init__(self):
        self.historial = []
        self.rehacer_pila = []
        
    def ejecutar_comando(self, comando):
        comando.ejecutar()
        self.historial.append(comando)
        self.rehacer_pila.clear()
        
    def deshacer(self):
        if self.historial:
            comando = self.historial.pop()
            comando.deshacer()
            self.rehacer_pila.append(comando)
        else:
            print("No hay comandos para deshacer.")
            
    def rehacer(self):
        if self.rehacer_pila:
            comando = self.rehacer_pila.pop()
            comando.ejecutar()
            self.historial.append(comando)
        else:
            print("No hay comandos para rehacer.")
            
# Ejemplo de uso
# Cliente
editor = EditorTexto()
admin = AdminComandos()

# Escribir texto
cmd1 = EscribirTextoCommand(editor, "Hola ")
cmd2 = EscribirTextoCommand(editor, "Joseph ")
cmd3 = EscribirTextoCommand(editor, "programador!")

admin.ejecutar_comando(cmd1)
admin.ejecutar_comando(cmd2)
admin.ejecutar_comando(cmd3)

editor.mostrar()  # Hola Joseph programador!

# Deshacer
admin.deshacer()
editor.mostrar()  # Hola Joseph 

# Otro deshacer
admin.deshacer()
editor.mostrar()  # Hola 

# Rehacer
admin.rehacer()
editor.mostrar()  # Hola Joseph 

# Nuevo texto (borra redo)
cmd4 = EscribirTextoCommand(editor, "🚀 en progreso")
admin.ejecutar_comando(cmd4)
editor.mostrar()  # Hola Joseph 🚀 en progreso

# Intentar rehacer (debería fallar)
admin.rehacer()  # ❌ Nada que rehacer.
