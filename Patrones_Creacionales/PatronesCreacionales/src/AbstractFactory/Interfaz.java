package AbstractFactory;

public class Interfaz {
    public static void crearInterfaz(GUIFactory factory) {
        Boton boton = factory.crearBoton();
        Ventana ventana = factory.crearVentana();
        boton.render();
        ventana.abrir();
    }
}
