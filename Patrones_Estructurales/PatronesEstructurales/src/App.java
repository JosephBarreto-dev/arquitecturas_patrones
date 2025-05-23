import Adapter.*;
import Composite.*;
import Decorator.*;
import Facade.*;
import Proxy.*;

public class App {
    public static void main(String[] args) throws Exception {
        //patron adapter
        System.out.println("\n____Patrón Adapter____");
        Pago pago = new PagoAdapter(new ExternalPaymentAPI());
        pago.pagar(500.0);

        //patron facade
        System.out.println("\n____Patrón Facade____");
        SistemaFactura sistemaFactura = new SistemaFactura();
        sistemaFactura.procesarFactura();

        //patron decorator
        System.out.println("\n____Patrón Decorator____");
        Mensaje mensaje = new Cifrado(new MensajeTexto());
        System.out.println(mensaje.enviar());

        //patron composite
        System.out.println("\n____Patrón Composite____");
        Panel panel = new Panel();
        panel.agregar(new Boton());
        panel.agregar(new Boton());

        Panel subPanel = new Panel();
        subPanel.agregar(new Boton());

        panel.agregar(subPanel);
        panel.mostrar();

        //patron proxy
        System.out.println("\n____Patrón Proxy____");
        BaseDatos dbInvitado = new ProxyBaseDatos(true);
        dbInvitado.leer();
        dbInvitado.escribir("Nuevo registro");

        BaseDatos dbAdmin = new ProxyBaseDatos(false);
        dbAdmin.escribir("Registro de admin");
        System.out.println("\n");
    }
}
