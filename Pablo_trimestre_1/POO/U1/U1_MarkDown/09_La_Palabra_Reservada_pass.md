# 9. LA PALABRA RESERVADA PASS
https://educacionadistancia.juntadeandalucia.es/centros/cordoba/pluginfile.php/365653/mod_resource/content/6/9_la_palabra_reservada_pass.html
---
En Python, la palabra reservada pass se usa como instrucción nula.

Es decir: no hace nada cuando se ejecuta.

¿Para qué sirve?
- Se utiliza como “relleno” cuando se necesita que exista una instrucción válida en un bloque de código, pero aún no quieres escribir nada allí.
- Evita que Python lance un error de sintaxis en lugares donde el lenguaje exige al menos una instrucción.

Ejemplos:

1. Clase vacía
```py
class MiClase:
    pass
```
 La clase existe, aunque no tenga atributos ni métodos.
 
2. Función vacía
```py
def funcion_por_hacer():
    pass
```
La función se puede definir, aunque aún no tenga código.

3. Condicional sin acción
```py
x = 10
if x > 0:
    pass  # No hacer nada si la condición es verdadera
else:
    print("x es negativo o cero")
```
