# 6. FUNCIONES ESPECIALES PARA TRABAJAR CON ATRIBUTOS
https://educacionadistancia.juntadeandalucia.es/centros/cordoba/pluginfile.php/365653/mod_resource/content/6/6_funciones_especiales_para_trabajar_con_atributos.html
---
Dentro de las funciones definidas de Python (built-in functions) existen varias para trabajar con los atributos o propiedades de un objeto. Estas funciones permiten la “manipulación dinámica de atributos” y son las siguientes:
- getattr(objeto, “atributo”). Retorna el atributo referenciado de ese objeto.
- hasattr(objeto, “atributo”). Retorna un boolean que indica si el objeto tiene o no ese atributo.
- delattr(objeto, “atributo”). Elimina el atributo del objeto.
- setattr(objeto, “atributo”, valor). Esta función no solo sirve para asignar un valor a un atributo sino que permite también añadir nuevos atributos a un objeto en tiempo de ejecución.

Estas funciones (getattr, hasattr, delattr, setattr) son súper útiles porque permiten trabajar con los atributos de los objetos de forma dinámica, es decir, sin saber sus nombres de antemano.

Aquí os dejo un ejemplo sencillo con una clase Persona:
```py
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```
El programa principal que usa esta clase podría ser el siguiente:
```py
from persona import Persona

# Crear un objeto
p1 = Persona("Ana", 25)

# ---------------------------
# 1. getattr(objeto, "atributo")
# ---------------------------
print("Nombre con getattr:", getattr(p1, "nombre"))   # "Ana"
print("Edad con getattr:", getattr(p1, "edad"))       # 25

# ---------------------------
# 2. hasattr(objeto, "atributo")
# ---------------------------
print("¿Tiene atributo 'nombre'? ->", hasattr(p1, "nombre"))   # True
print("¿Tiene atributo 'altura'? ->", hasattr(p1, "altura"))   # False

# ---------------------------
# 3. setattr(objeto, "atributo", valor)
# ---------------------------
setattr(p1, "edad", 30)       # Modifica un atributo existente
setattr(p1, "altura", 1.70)   # Crea un nuevo atributo dinámicamente
print("Edad modificada:", p1.edad)
print("Nueva altura añadida:", p1.altura)

# ---------------------------
# 4. delattr(objeto, "atributo")
# ---------------------------
delattr(p1, "altura")         # Elimina el atributo "altura"
print("¿Tiene atributo 'altura' después de borrar? ->", hasattr(p1, "altura"))
```

Python permite alterar el número de atributos de un objeto de forma dinámica, tanto dentro como fuera de la definición de la clase. Este cambio en el número de atributos implica tanto la eliminación (como se vio en el apartado 8) como la adición de atributos nuevos.

Para añadir un atributo nuevo a un objeto basta con utilizar la sintaxis “objeto.atributo = valor”.

Llegados a este punto, para conocer todos los atributos de un objeto puede usarse el atributo __dict__ que posee todo objeto. Este atributo contiene un diccionario con las parejas nombre de atributo y valor.
