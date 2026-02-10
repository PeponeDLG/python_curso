# 2. ATRIBUTOS DE INSTANCIA Y DE CLASE
https://educacionadistancia.juntadeandalucia.es/centros/cordoba/pluginfile.php/365653/mod_resource/content/6/2_atributos_de_instancia_y_de_clase.html
---
Al trabajar con clases y objetos podemos encontrarnos con dos tipos de atributos: de instancia y de clase.

- Los atributos de instancia son propios de cada instancia (de cada objeto). Si existen varios objetos de la clase “Empleado”, cada uno de ellos tendrá un valor para el nombre, salario, correo, etc.
- Sin embargo, los atributos de clase son compartidos por todos los objetos de esa clase.

En el siguiente ejemplo, podemos usar un atributo de clase llamado contador que se incremente cada vez que se cree un nuevo objeto de la clase Coche.
```py
# Definición de una clase

class Coche:
     # Atributo de clase (contador de instancias)
    contador = 0

    # Método contructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
        
        # Cada vez que se crea un coche, el contador de la clase aumenta en 1
        Coche.contador += 1
    
    def acelerar(self):
        self.velocidad += 5

    def frenar(self):
        self.velocidad -= 5
    
    def getInfo(self):
        info = "------Información del coche------"
        info += f"\nColor: {self.color}\nMarca: {self.marca}\nModelo: {self.modelo}\nVelocidad: {self.velocidad}\nCaballaje: {self.caballaje}\nPlazas: {self.plazas}" 
        return info
    
# fin de la definición de la clase
```

- Para acceder al valor de un atributo de clase desde dentro de la clase se utiliza el nombre de la clase y el nombre del atributo (ver línea 17 del ejemplo).
- Sin embargo, desde fuera de la clase puede accederse al valor de estos atributos de clase utilizando tanto el nombre de la clase como el nombre de cualquier instancia de la misma (línea 18 del ejemplo).

Observa el siguiente código:
```py
# Importamos la clase Coche desde el archivo coche.py
from coche import Coche

# Creamos distintos objetos de la clase Coche con valores personalizados
coche1 = Coche("Amarillo", "Ferrari", "Aventador", 300, 500, 2)
coche2 = Coche("Verde", "Porsche", "911", 250, 400, 2)
coche3 = Coche("Negro", "Lamborghini", "Aventador", 300, 500, 2)
coche4 = Coche("Rosa", "Seat", "Ibiza", 250, 200, 5)

# Mostramos la información de cada coche usando el método getInfo()
print(coche1.getInfo())
print(coche2.getInfo())
print(coche3.getInfo())
print(coche4.getInfo())

# Atributo de clase
print(f"Se han creado {Coche.contador} coches en total")  # Acceso a un atributo de clase desde la clase
print(f"Se han creado {coche1.contador} coches en total") # Acceso a un atributo de clase desde una instancia 
```
