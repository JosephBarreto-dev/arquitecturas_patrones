import Builder.*;
import Prototype.*;
import Singleton.*;
import Factory.*;
import AbstractFactory.*;

public class App {
    public static void main(String[] args) throws Exception {

        System.out.println("\n____Patrón Singleton____");
        ConexionBD bd1 = ConexionBD.getInstancia();
        ConexionBD bd2 = ConexionBD.getInstancia();
        bd1.consultar("SELECT * FROM productos");
        System.out.println("¿Misma instancia? " + (bd1 == bd2));  // true

        System.out.println("\n____FACTORY____");
        Usuario cliente = UsuarioFactory.crearUsuario("cliente");
        Usuario admin = UsuarioFactory.crearUsuario("admin");
        cliente.mostrarTipo();
        admin.mostrarTipo();

        System.out.println("\n____ABSTRACT FACTORY____");
        GUIFactory windowsGUI = new WindowsFactory();
        Interfaz.crearInterfaz(windowsGUI);

        System.out.println("\n____Patrón Builder____");
        OrdenCompra orden = new OrdenCompra.Builder("Laptop")
                .cantidad(2)
                .direccionEnvio("Calle 123")
                .envioExpress(true)
                .build();
        orden.mostrar();

        System.out.println("\n____Patrón Prototype____");
        LogMensaje log1 = new LogMensaje("INFO", "Inicio de aplicación");
        LogMensaje log2 = log1.clonar();
        log2.mostrar();
    }
}
