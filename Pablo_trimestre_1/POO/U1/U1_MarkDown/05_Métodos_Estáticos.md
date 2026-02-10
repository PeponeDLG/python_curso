# MÉTODOS ESTÁTICOS
https://educacionadistancia.juntadeandalucia.es/centros/cordoba/pluginfile.php/365653/mod_resource/content/6/5_mtodos_estticos.html
---
Puede decirse que un método estático es una función definida a nivel de clase.

Está asociado a la clase antes que a los objetos de la misma.

Son llamados utilizando el nombre de la clase, y además no pueden alterar el estado de un objeto ni los atributos de clase.

Los métodos estáticos se diferencian de los métodos de clase en que los primeros no operan con los atributos de clase. Se utilizan en alguna de estas situaciones:
- Cuando se quiere implementar una funcionalidad que no depende de ningún atributo de la clase ni de una instancia en particular de la clase.
- Por motivos de organización del código de la aplicación. Puede crearse una clase que contenga una o varias funciones que serán utilizadas en varios puntos de la aplicación.

En Python un método estático se crea con el decorador “@staticmethod”.

Un ejemplo de método estático en Python puede ser el siguiente:
```py
class Calculadora:
    # Método estático: no usa ni self ni cls
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def es_par(numero):
        return numero % 2 == 0


# Uso del método estático
print(Calculadora.sumar(10, 5))   # 15
print(Calculadora.es_par(8))      # True
print(Calculadora.es_par(7))      # False

# También se puede llamar desde una instancia
calc = Calculadora()
print(calc.sumar(3, 4))  # 7
```
- sumar(a, b) y es_par(numero) no dependen del estado de la clase ni de un objeto, por eso son estáticos.
- Se pueden invocar tanto desde la clase como desde una instancia, pero lo normal es usarlos directamente desde la clase.

Vamos a añadir un método estático a la clase Coche.
- Un ejemplo útil sería un método que verifique si un número de plazas es válido para un coche (por ejemplo, entre 1 y 9 plazas).
```py
class Coche:
    # Atributo de clase (contador de instancias)
    contador = 0

    # Método constructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.__marca = marca
        self.__modelo = modelo
        self._velocidad = velocidad
        self._caballaje = caballaje
        self._plazas = plazas

        # Incrementamos el contador cada vez que se crea un coche
        Coche.contador += 1

    # Métodos de instancia
    def acelerar(self):
        self._velocidad += 5

    def frenar(self):
        self._velocidad -= 5

    def getInfo(self):
        info = "------ Información del coche ------"
        info += f"\nColor: {self.color}\nMarca: {self.__marca}\nModelo: {self.__modelo}\nVelocidad: {self._velocidad}\nCaballaje: {self._caballaje}\nPlazas: {self._plazas}" 
        return info

    # Método de clase
    @classmethod
    def get_num_coches(cls):
        return cls.contador

    # Método estático
    @staticmethod
    def plazas_validas(plazas):
        """Verifica si el número de plazas es válido para un coche"""
        return 1 <= plazas <= 9
```
Mostramos un ejemplo de uso de la clase Coche:
```py
# Importamos la clase Coche desde el archivo coche.py
from coche import Coche

# Podemos usar el método estático sin crear ningún coche
print(Coche.plazas_validas(4))   # True
print(Coche.plazas_validas(12))  # False

# Creamos coches solo si las plazas son válidas
if Coche.plazas_validas(5):
    coche1 = Coche("Rojo", "Ferrari", "Aventador", 300, 500, 2)
    print(coche1.getInfo())

print(f"Se han creado {Coche.get_num_coches()} coche(s).")
```
