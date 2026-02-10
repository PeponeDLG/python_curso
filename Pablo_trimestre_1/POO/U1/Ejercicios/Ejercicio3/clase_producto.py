# Define la clase con su constructor y un método.
# Prueba la clase y sus métodos instanciando objetos y aplicándole los métodos

class Producto:
    # Método mágico constructor que sirve para instanciar objetos
    def __init__(self, nombre, precio, stock):
        # Atributos
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Muestra los datos de un producto
    def mostrar_producto(self):
        print(f"Nombre: {self.nombre}, precio: {self.precio}, stock: {self.stock}")

    # Muestra el valor total del inventario de un producto
    def calcular_valor_inventario(self):
        print(f"Valor total del stock de {self.nombre}: {self.precio * self.stock}€")

# Crea varias instancias de productos de prueba
producto_1 = Producto("Pelota", 10, 100)
producto_2 = Producto("Cuchara", 3, 40)
producto_3 = Producto("Vaso", 8, 120)

# Prueba el método mostrar_producto()
producto_1.mostrar_producto()

# Prueba el método calcular_valor_inventario()
producto_1.calcular_valor_inventario()
