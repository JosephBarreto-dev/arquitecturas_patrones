from domain.orden import Orden
from adapters.mongo_repo import MongoRepositorioOrden
from adapters.stripe_adapter import StripeServicioPago

def main():
    productos = ["Teclado", "Mouse"]
    total = 120.00
    orden = Orden(productos, total)

    repo = MongoRepositorioOrden()
    pago = StripeServicioPago()

    if pago.procesar_pago(orden):
        orden.marcar_como_pagada()
        repo.guardar(orden)
        print("Orden pagada y guardada con exito.")
    else:
        print("Error al procesar el pago")

if __name__ == "__main__":
    main()
