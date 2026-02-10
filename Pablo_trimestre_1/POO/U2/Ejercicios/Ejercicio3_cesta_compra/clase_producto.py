class Producto:
    # Cada producto se inicializa con una cantidad que servirá de contador de unidades
    def __init__(self, nombre, precio:float, cantidad=1):
        if precio < 0:
            raise ValueError("El precio tiene que ser mayor que 0")
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = 1

    def __str__(self):
        return f"Producto(nombre='{self.__nombre}', precio={self.__precio}"

    def __eq__(self, otro):
        if not isinstance(otro, Producto):
            return False
        return self.get_nombre == otro.get_nombre

    # Getters y setters
    @property
    def get_nombre(self):
        return self.__nombre

    @property
    def get_precio(self):
        return self.__precio
    
    @property
    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad
