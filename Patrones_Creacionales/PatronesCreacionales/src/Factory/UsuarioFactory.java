package Factory;

public class UsuarioFactory {
    public static Usuario crearUsuario(String tipo) {
        return switch (tipo.toLowerCase()) {
            case "cliente" -> new Cliente();
            case "admin" -> new Administrador();
            case "operador" -> new Operador();
            default -> throw new IllegalArgumentException("Tipo desconocido");
        };
    }
}
