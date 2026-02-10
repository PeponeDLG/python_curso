# 1. CLASE Y OBJETOS
https://educacionadistancia.juntadeandalucia.es/centros/cordoba/pluginfile.php/365653/mod_resource/content/6/11_propiedades_y_mtodos.html
---
Además, la Programación Orientada a Objetos (POO) está basada el la forma en la que concebimos la realidad e interactuamos con ella, por lo que seguro que el método aquí trabajado te va a resultar familiar.
Piensa que el mundo que nos rodea está todo (o casi) formado por objetos: sillas, pantallas, coches, puertas...

Y, ¿qué tienen en común todos estos objetos?
- Que están formados por rasgos que los definen (características)
- y por acciones que pueden realizar (funciones). Para ir comenzando a activar esta nueva visión, te será de gran utilidad comenzar a practicar con las siguientes reflexiones y ejercicios.

### POO a nuestro alrededor
Piensa en un objeto de nuestra vida diaria como es el coche y en qué te fijarías si tuvieras que definir las diferencias y similitudes entre unos y otros. Observa la imagen que acompaña para ayudarte y proporciona un modelo básico indicando:
- Cinco características que definen un coche.
- Cinco acciones que pueda realizar.

### Introducción
La programación orientada a objetos (POO) es un paradigma de programación (estilo o forma de programar) que se basa en la utilización de objetos similares a los de la vida real, con sus características y comportamiento.

Python es un lenguaje orientado a objetos.

Un objeto se caracteriza por tener propiedades y métodos o dicho de otra forma, datos y código.
- Las propiedades describen el estado del objeto
- y los métodos aportan funcionalidad al mismo.

Una clase define de forma genérica cómo serán los objetos de un tipo determinado.

En nuestro ejemplo, existirá por tanto una clase llamada “Coche” que definirá las características o atributos de los que consta cada coche.

Los objetos serían cada uno de los coches reales y que se ajustan a la estructura definida, es decir, a la clase.

Podemos imaginar a una clase como una plantilla en base a la cual se construyen objetos.

El proceso de creación de objetos se conoce como “instanciación”. Se dice que un objeto es una “instancia” de una clase.

Las ventajas que aporta esta forma de programar son:
- la reutilización de código,
- la organización modular de las aplicaciones
- el encapsulamiento,
- abstracción, 
- herencia

## 1.1 Propiedades y métodos
- Las propiedades o atributos de un objeto determinan el estado del mismo.
- Los métodos son acciones que puede llevar a cabo un objeto y que pueden alterar o no su estado.

Los métodos son funciones definidas en la clase y que pueden servir para instanciar (crear) el objeto, modificar el estado del mismo (cambiar el valor de algún atributo), obtener o retornar el valor de algún atributo o interactuar con otros objetos.

Imaginemos ahora una aplicación que debe trabajar con vehículos.

Podríamos crear una clase “Vehículo”.
- Sus atributos serían matrícula, marca, modelo, potencia y combustible.
- Sus métodos podrían ser es_diesel y letras_matricula, que retornan si es vehículo en cuestión es diesel o no y las letras de su matrícula respectivamente.

De esta forma el vehículo con matrícula 1290-BMZ, marca Seat, modelo Ibiza, con 100 cv y diésel sería un objeto perteneciente a la clase “Vehiculo” creada.

La abstracción es uno de los conceptos básicos vinculados a la POO. Mediante la abstracción, un usuario final de una clase puede utilizar sus métodos sin la necesidad de conocer cómo han sido desarrollados o implementados.

### Creación de una clase en python
En el siguiente ejemplo se ve claramente como podemos crear una clase en python:
```py
# Programación orientada a objetos

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

1.- Se define una clase llamada Coche, que actúa como una plantilla para crear objetos.
- Dentro de la clase se establecen varios atributos (color, marca, modelo, velocidad, caballaje y número de plazas) que describen las características de un coche.
- La clase también contiene métodos (funciones propias de la clase):
U- no para acelerar, que aumenta la velocidad.
- Otro para frenar, que la disminuye.
- Y uno más para consultar la velocidad actual.

2.- Después se crea un objeto (o instancia) de la clase llamado coche1. Este objeto hereda todas las propiedades y comportamientos definidos en la clase.

3.- Se accede primero a sus atributos, mostrando en pantalla el color, la marca, el modelo, la velocidad inicial, el caballaje y las plazas del coche.

4.- Luego se usan los métodos: el coche acelera, aumentando su velocidad en 5, y después frena, reduciéndola nuevamente en 5. Cada vez que se realiza una de estas acciones, se muestra la velocidad actual del coche.

La salida del programa muestra primero las propiedades del coche, y después cómo cambia la velocidad al acelerar y frenar

## 1.2 El método constructor
La función __init__() es el método constructor de la clase.

Esta función recibe varios argumentos.
- El primero, “self”, hace referencia al propio objeto que se está creando.
- El resto de argumentos guardan los valores que se darán a cada uno de los atributos del objeto que se crea.
- Por norma, se utiliza el mismo nombre para argumentos y atributos. Dentro del constructor los atributos van precedidos de la palabra reservada “self”.

Ejemplo de uso del constructor para la clase Coche:
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

Se define una clase llamada Coche, que sirve como plantilla para crear objetos de tipo coche.
- La clase tiene varios atributos: color, marca, modelo, velocidad, caballaje y número de plazas.
- Se incluye un constructor (__init__) que permite crear coches con valores personalizados para cada atributo en el momento de instanciarlos.
- La clase define métodos de comportamiento:
    - acelerar → aumenta la velocidad en 5.
    - frenar → disminuye la velocidad en 5.
- También tiene un método getInfo que devuelve un texto con toda la información del coche (sus atributos).

En el siguiente código, se muestra como crear objetos de la clase Coche. Es en este momento de la creación cuando se reserva memoria para los objetos.
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
- Primero se importa la clase Coche desde otro archivo llamado coche.py.
- Se crean cuatro objetos (coche1, coche2, coche3, coche4) con diferentes valores de color, marca, modelo, velocidad, caballaje y plazas.
- Finalmente, se llama al método getInfo() de cada coche para mostrar en pantalla toda su información.
