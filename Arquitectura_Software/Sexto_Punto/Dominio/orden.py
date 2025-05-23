class Orden:
    def __init__(self, productos: list, total: float):
        self.productos = productos
        self.total = total
        self.pagada = False

    def marcar_como_pagada(self):
        self.pagada = True
