package Proxy;

public class ProxyBaseDatos implements BaseDatos {
    private BaseDatosReal baseDatos;
    private boolean accesoAutorizado;

    public ProxyBaseDatos(boolean accesoAutorizado) {
        this.accesoAutorizado = accesoAutorizado;
        this.baseDatos = new BaseDatosReal();
    }
    
    public void leer() {
        baseDatos.leer();
    }
    public void escribir(String datos) {
        if(accesoAutorizado) {
            baseDatos.escribir(datos);
        }else{
            System.out.println("Acceso denegado. No se puede escribir en la base de datos.");
        }
    }
}
