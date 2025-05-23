from ports.servicio_pago import ServicioPago

class StripeServicioPago(ServicioPago):
    def procesar_pago(self, orden):
        print(f"[Stripe Simulado] Procesando pago de ${orden.total}")
        return True
