from abc import ABC, abstractmethod # ABC es el padre de todas las clases abstractas en Python

# Clase abstracta. Hereda de ABC para poder ser abstracta en Python.
class Persona(ABC):
    def __init__(self, nombre:str, apellidos:str, correo:str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena")
        elif not isinstance(apellidos, str):
            raise ValueError("Los apellidos deben ser una cadena")
        elif not isinstance(correo, str):
            raise ValueError("El correo debe ser una cadena")
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__correo = correo

    def __str__(self):
        return f"Nombre: {self.__nombre} - Apellidos: {self.__apellidos} - Correo: {self.__correo}"

    # Getters y Setters al estilo pythónico
    # Fuente: https://docs.python.org/es/3.14/library/functions.html
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellidos(self):
        return self.__apellidos

    @property
    def correo(self):
        return self.__correo

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @apellidos.setter
    def apellidos(self, value):
        self.__apellidos = value

    @correo.setter
    def correo(self, value):
        self.__correo = value
