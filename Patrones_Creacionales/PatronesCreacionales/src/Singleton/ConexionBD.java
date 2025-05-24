package Singleton;

public class ConexionBD {
    private static ConexionBD instancia;

    private ConexionBD() {
        System.out.println("Conexión a la base de datos establecida.");
    }

    public static synchronized ConexionBD getInstancia() {
        if (instancia == null) {
            instancia = new ConexionBD();
        }
        return instancia;
    }

    public void consultar(String sql) {
        System.out.println("Ejecutando consulta: " + sql);
    }
}
