package AbstractFactory;

public class LinuxFactory implements GUIFactory {
    public Boton crearBoton() {
        return new BotonLinux();
    }

    public Ventana crearVentana() {
        return new VentanaLinux();
    }
}
