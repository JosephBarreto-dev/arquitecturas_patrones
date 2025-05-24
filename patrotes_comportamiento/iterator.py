class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - {self.categoria} - ${self.precio}"

class ColeccionProductos:
    def __init__(self):
        self._productos = []

    def agregar(self, producto):
        self._productos.append(producto)

    def __iter__(self):
        return iter(self._productos)  # Iterador estándar

    def iterar_por_categoria(self, categoria):
        return (p for p in self._productos if p.categoria == categoria)

    def iterar_por_precio_menor_a(self, max_precio):
        return (p for p in self._productos if p.precio < max_precio)

# Crear productos
p1 = Producto("Laptop", "Electrónica", 1200)
p2 = Producto("Cámara", "Electrónica", 800)
p3 = Producto("Libro", "Libros", 25)
p4 = Producto("Auriculares", "Electrónica", 50)
p5 = Producto("Cuaderno", "Papelería", 10)

# Crear colección
coleccion = ColeccionProductos()
for p in [p1, p2, p3, p4, p5]:
    coleccion.agregar(p)

# Recorrido normal
print("📋 Todos los productos:")
for p in coleccion:
    print(p)

# Filtro por categoría
print("\n📂 Solo electrónicos:")
for p in coleccion.iterar_por_categoria("Electrónica"):
    print(p)

# Filtro por precio
print("\n💸 Productos por menos de $100:")
for p in coleccion.iterar_por_precio_menor_a(100):
    print(p)
