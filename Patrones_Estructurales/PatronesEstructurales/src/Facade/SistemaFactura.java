package Facade;

public class SistemaFactura {
    private GenerarFactura generador = new GenerarFactura();
    private EnviarFactura enviador = new EnviarFactura();
    private RegistrarFactura registrador = new RegistrarFactura();

    public void procesarFactura() {
        generador.generar();
        registrador.registrar();
        enviador.enviar();
    }
}
