# MÉTODOS MÁGICOS O DUNDER (DOUBLE UNDERSCORE)
https://educacionadistancia.juntadeandalucia.es/centros/cordoba/pluginfile.php/365653/mod_resource/content/6/7_mtodos_mgicos_o_dunder_double_underscore.html
---
Son funciones definidas a nivel de clase, y su nombre comienza y termina con doble guión bajo (__). Aunque pueden ser invocados, suelen ser llamados por Python en situaciones especiales.

Algunos ejemplos de estos métodos son:
- __init__(). Es llamado cuando se construye un objeto.
- __str__(). Retorna una cadena destinada a los usuarios, que representa al objeto.
- __repr__(). Retorna una cadena destinada a los programadores, que representa al objeto.
- __eq__(). Método para comparar dos objetos. “eq” viene de “equals”.
- __del__(). Conocido como el destructor de un objeto. Es llamado cuando todas las referencias a un objeto han sido eliminadas.

En el siguiente ejemplo usamos varios objetos mágicos en la clase Persona:
```py
class Persona:
    # __init__(): se ejecuta al crear un objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Objeto Persona creado: {self.nombre}, {self.edad} años")

    # __str__(): representación para el usuario (informal, legible)
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

    # __repr__(): representación para el programador (más técnica)
    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

    # __eq__(): permite comparar dos objetos con "=="
    def __eq__(self, otro):
        if isinstance(otro, Persona):
            return self.nombre == otro.nombre and self.edad == otro.edad
        return False

    # __del__(): destructor, llamado cuando se elimina el objeto
    def __del__(self):
        print(f"Objeto Persona eliminado: {self.nombre}")
```
Para hacer uso de esta clase, podemos usar el siguiente programa principal:
```py
# Importar la clase
from persona import Persona

# __init__() se ejecuta al crear los objetos
p1 = Persona("Ana", 25)
p2 = Persona("Luis", 30)
p3 = Persona("Ana", 25)

# __str__(): representación legible para el usuario
print("Usando __str__():", str(p1))   # "Ana, 25 años"

# __repr__(): representación para el programador
print("Usando __repr__():", repr(p1)) # "Persona(nombre='Ana', edad=25)"

# __eq__(): comparación de objetos
print("¿p1 == p2?", p1 == p2)   # False
print("¿p1 == p3?", p1 == p3)   # True

# __del__(): se llama cuando el objeto deja de existir
del p2   # fuerza la eliminación de p2
```
