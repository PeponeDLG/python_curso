# Ejemplo pythónico de clase con getter y setter
# https://docs.python.org/3/library/functions.html
# https://www.luisllamas.es/python-como-usar-propiedades/

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}. Edad: {self.edad}"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and edad > 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un número entero positivo")

# Ejemplos de uso
print("Uso del Setter:")
p1 = Persona("Paco", 30)
print(p1)
p1.nombre = "Rafa"
print(p1)

print("Uso del Getter:")
print(p1.nombre)
