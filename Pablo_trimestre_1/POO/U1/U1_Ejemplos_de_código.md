# UT1.- POO - INTRODUCCIÓN Y ESTRUCTURA BÁSICA
## Ejemplos de código
https://educacionadistancia.juntadeandalucia.es/centros/cordoba/pluginfile.php/365653/mod_resource/content/6/11_propiedades_y_mtodos.html
---
### Creación de una clase en python
```py
# Definición de una clase

class Coche:
    # Atributos o propiedades (variables)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Metodos (funciones)
    def acelerar(self):
        self.velocidad += 5

    def frenar(self):
        self.velocidad -= 5
    
    def getVelocidad(self):
        return self.velocidad
    
# fin de la definición de la clase

# Creación de un objeto o instancia de la clase
coche1 = Coche()

# Acceder a los atributos y métodos
print("Acceso a la propiedades")
print(coche1.color)
print(coche1.marca)
print(coche1.modelo)
print(coche1.velocidad)
print(coche1.caballaje)
print(coche1.plazas)

# Acceder a los métodos
print("\nAcceso a los metodos")
coche1.acelerar()
print (coche1.getVelocidad())
coche1.frenar()
print(coche1.getVelocidad())
```

### 1.2 El método constructor
```py
# Definición de una clase

class Coche:

    # Método contructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    def acelerar(self):
        self.velocidad += 5

    def frenar(self):
        self.velocidad -= 5
    
    def getInfo(self):
        info = "------Información del coche------"
        info += f"\nColor: {self.color}\nMarca: {self.marca}\nModelo: {self.modelo}\nVelocidad: {self.velocidad}\nCaballaje: {self.caballaje}\nPlazas: {self.plazas}" 
        return info
    
# fin de la definción de la clase
```

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
```

### Atributos de instancia y de clase
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

TODO


```py

```
