from clase_producto import Producto

class GestionAlmacen:

    # Atributo de clase para guardar los productos creados
    productos = [
        Producto(1, "Pelota", "Deportes", 20, 54, 10),
        Producto(2, "Teclado", "Electronica", 30, 4, 5)
    ]

    # Métodos de clase (se aplican a la clase, no a una instancia de la misma)

    # Introduce un nuevo producto
    @classmethod
    def nuevo_producto(cls, producto):
        # Comprueba que es un producto
        if not isinstance(producto, Producto):
            raise Exception("No es un producto")

        # Comprueba que no está en la lista de productos
        if producto in cls.productos:
            return False

        # Inserta el nuevo producto
        cls.productos.append(producto)
        return True

    # Busca un producto de la lista por su identificador y si lo encuentra lo devuelve
    # Si no, devuelve False
    @classmethod
    def buscar_por_id(cls, id):
        for producto in cls.productos:
            if cls.producto.get_identoficador == id:
                return producto
            return False
        
    # Devuelve una lista de productos cuyo stock está por debajo del mínimo
    @classmethod
    def bajo_minimos(cls):
        minimos = []
        for producto in cls.productos:
            if producto.get_stock < producto.get_stock_minimo:
                minimos.append(producto)

        return minimos

    # Lista los productos existentes
    @classmethod
    def listado(cls):
        for producto in cls.productos:
            print(f"{producto.get_nombre}")
