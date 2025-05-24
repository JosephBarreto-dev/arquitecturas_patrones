package Adapter;

public class PagoAdapter implements Pago {
    private ExternalPaymentAPI api;

    public PagoAdapter(ExternalPaymentAPI api) {
        this.api = api;
    }

    @Override
    public void pagar(double cantidad) {
        api.realizarPago(cantidad);
    }
}
