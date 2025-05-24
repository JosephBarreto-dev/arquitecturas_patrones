package AbstractFactory;

public class WindowsFactory implements GUIFactory {
    public Boton crearBoton() {
        return new BotonWindows();
    }

    public Ventana crearVentana() {
        return new VentanaWindows();
    }
}
