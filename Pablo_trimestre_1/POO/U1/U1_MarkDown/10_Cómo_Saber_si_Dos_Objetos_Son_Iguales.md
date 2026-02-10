# 10. CÓMO SABER SI DOS OBJETOS SON IGUALES
https://educacionadistancia.juntadeandalucia.es/centros/cordoba/pluginfile.php/365653/mod_resource/content/6/10_cmo_saber_si_dos_objetos_son_iguales.html
---
Escenario 1. Partimos de dos referencias y queremos determinar si apuntan a la misma dirección de memoria.
- Para ello hacemos uso de los operadores “is” y “not is” que determinan si dos referencias apuntan a la misma dirección de memoria.
- En este caso, a y b apuntan al mismo dato. La pregunta "a is b" retorna True.
- El método id(objeto) retorna un identificador único del objeto almacenado en memoria.

Escenario 2. Partimos de dos objetos y queremos determinar si sus atributos son iguales. En este caso, debemos definir el método __eq__ en la clase y dentro de él comparar por parejas los atributos de ambos objetos. Este método retorna True en caso de que todas las comparaciones sean True.
```py
# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: {self.nombre} {self.edad}'

    def __eq__(self, value):
        return self.nombre == value.nombre and self.edad == value.edad


# Uso de la clase
x = Persona("Juan", 25)
y = Persona("Juan", 25)

# Comparaciones
print(x is y)   # False -> Son objetos diferentes en memoria
print(x == y)   # True  -> Son iguales según __eq__()
```
Observa como el operador “is” retorna False y la comparación mediante “==” retorna True. Son objetos distintos pero guardan los mismos valores en sus atributos.
