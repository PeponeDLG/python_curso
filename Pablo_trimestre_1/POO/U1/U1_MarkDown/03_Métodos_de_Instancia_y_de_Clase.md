# 3. MÉTODOS DE INSTANCIA Y DE CLASE
https://educacionadistancia.juntadeandalucia.es/centros/cordoba/pluginfile.php/365653/mod_resource/content/6/3_mtodos_de_instancia_y_de_clase.html
---
Igual que los atributos, los métodos pueden ser de instancia y de clase.

- Los primeros permiten el acceso a los atributos de la instancia.
- Los métodos de clase, por su parte, proporcionan acceso a los atributos de la clase.

Un método de clase va precedido del decorador “@classmethod” y no puede acceder a los atributos de instancia. Además, recibe la clase de forma implícita como primer argumento.

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
    
    # Método de clase para obtener el número de coches creados
    @classmethod
    def get_num_coches(cls):
        return cls.contador
    
# fin de la definción de la clase
```
- get_num_coches es un método de clase, por lo que accede a cls.contador (la clase misma).
- Puede llamarse tanto desde la clase (Coche.get_num_coches()) como desde una instancia (coche1.get_num_coches()).

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

# Usamos el método de clase para saber cuántos coches hay
print(f"Se han creado {Coche.get_num_coches()} coches en total")

# También se puede llamar desde una instancia
print(f"(Usando coche1) Número de coches creados: {coche1.get_num_coches()}")
```
