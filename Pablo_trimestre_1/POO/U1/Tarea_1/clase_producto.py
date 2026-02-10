# Definición de la clase Producto con sus propios atributos y métodos

class Producto:

    # Método constructor (método mágico)
    def __init__(self, identificador, nombre, categoria, precio, stock, stock_minimo):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__stock = stock
        self.__stock_minimo = stock_minimo

    # Método getter de ejemplo
    @property
    def get_categoria(self):
        return self.__categoria

    # Método mágico para mostrar datos de un producto
    def __str__(self):
        return f"Id: {self.__identificador}\nNombre: {self.__nombre}\nStock: {self.__stock}"

    # Otros métodos
    def actualizar_stock(self, num_unidades: int):
        if not isinstance(num_unidades, int):
            raise Exception("El número de unidades debe ser un entero")

        self.__stock += num_unidades

    def esta_en_minimos(self):
        return self.__stock < self.__stock_minimo

    def __eq__(self, other):
        return self.__identificador == other.__identificador
