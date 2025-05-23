package Proxy;

public class BaseDatosReal implements BaseDatos {
    public void leer() {
    System.out.println("Leyendo datos de la base de datos real.");
    }
    public void escribir(String datos) {
        System.out.println("Escribiendo en la base de datos: " + datos);
    }
}
