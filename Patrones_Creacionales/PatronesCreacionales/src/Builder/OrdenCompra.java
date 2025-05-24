package Builder;

public class OrdenCompra {
    private final String productos;
    private final int cantidad;
    private final boolean envioExpress;
    private final String direccionEnvio;

    private OrdenCompra(Builder builder){
        this.productos = builder.productos;
        this.cantidad = builder.cantidad;
        this.envioExpress = builder.envio;
        this.direccionEnvio = builder.direccionEnvio;
    }

    public static class Builder {
        private String productos;
        private int cantidad = 1;
        private boolean envio = false;
        private String direccionEnvio = "No especificada";

        public Builder(String productos) {
            this.productos = productos;
        }
        public Builder cantidad(int cantidad) {
            this.cantidad = cantidad;
            return this;
        }
        public Builder envioExpress(boolean envio) {
            this.envio = envio;
            return this;
        }
        public Builder direccionEnvio(String direccionEnvio) {
            this.direccionEnvio = direccionEnvio;
            return this;
        }

        public OrdenCompra build() {
            return new OrdenCompra(this);
        }
    }

    public void mostrar() {
        System.out.println("Orden de compra:");
        System.out.println("Productos: " + productos);
        System.out.println("Cantidad: " + cantidad);
        System.out.println("envío express: " + envioExpress);
        System.out.println("dirección de envío: " + direccionEnvio);
    }
}
