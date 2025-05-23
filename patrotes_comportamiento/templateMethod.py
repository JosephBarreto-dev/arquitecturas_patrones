from abc import ABC, abstractmethod

class TareaAutomatizada(ABC):
    def ejecutar(self):
        self.iniciar()
        self.realizar_tarea()
        self.finalizar()

    def iniciar(self):
        print("✅ Iniciando tarea...")

    @abstractmethod
    def realizar_tarea(self):
        pass

    def finalizar(self):
        print("🏁 Tarea completada.\n")

class BackupBaseDatos(TareaAutomatizada):
    def realizar_tarea(self):
        print("💾 Realizando backup de la base de datos...")

class LimpiarTemporales(TareaAutomatizada):
    def realizar_tarea(self):
        print("🧼 Borrando archivos temporales...")

class LimpiarConLogs(TareaAutomatizada):
    def realizar_tarea(self):
        print("🗑 Eliminando archivos antiguos...")
        print("📝 Guardando logs de limpieza...")

tareas = [
    BackupBaseDatos(),
    LimpiarTemporales(),
    LimpiarConLogs()
]

for tarea in tareas:
    tarea.ejecutar()
