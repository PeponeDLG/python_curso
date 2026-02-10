# ENCAPSULAIENTO
https://educacionadistancia.juntadeandalucia.es/centros/cordoba/pluginfile.php/365653/mod_resource/content/6/4_encapsulamiento.html
---
El encapsulamiento es un mecanismo que permite ocultar o limitar el acceso a las propiedades y métodos de un objeto desde el exterior. Este acceso solo estará disponible a través de determinados métodos, con lo que se consigue proteger al objeto frente a posibles cambios no deseados.

En algunos lenguajes de programación este control de acceso se implementa a nivel de clase, mediante modificadores que indican cuando una propiedad o método es público, privado o protegido.
- Un elemento privado es accesible solo desde dentro de la clase.
- Sin embargo, si está declarado como público puede ser accedido desde el exterior.
- Si el atributo o método es protegido significa que es accesible desde dentro de la clase y de las subclases que heredan de esta.

En Python esta posibilidad no existe, todo lo definido en una clase es público por defecto y por tanto accesible desde el exterior. Para conseguir que algún elemento de una clase sea considerado protegido o privado, Python ha adoptado las convenciones siguientes:
- Si el nombre del atributo/método va precedido de un guión bajo (_), se le considera protegido.
- Si el nombre del atributo/método va precedido de un doble guión bajo (__), se le considera privado.

Será el propio programador el que decidirá si seguir o no estas convenciones. Es necesario mencionar que los atributos siempre son accesibles desde el exterior de esta forma:
- Atributo protegido: objeto._atributo.
- Atributo oculto: objeto._Clase__atributo.

Modificamos nuestra clase Coche, definiendo diferentes tipos de atributos:
```py
# Definición de una clase

class Coche:
     # Atributo de clase (contador de instancias)
    contador = 0

    # Método contructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        
        self.color = color # Atributo de instancia
        self.__marca = marca # Atributo privado
        self.__modelo = modelo # Atributo privado
        self._velocidad = velocidad # Atributo protegido
        self._caballaje = caballaje # Atributo protegido
        self._plazas = plazas # Atributo protegido
        
        # Cada vez que se crea un coche, el contador de la clase aumenta en 1
        Coche.contador += 1
    
    def acelerar(self):
        self.velocidad += 5

    def frenar(self):
        self.velocidad -= 5
    
    def getInfo(self):
        info = "------Información del coche------"
        info += f"\nColor: {self.color}\nMarca: {self.__marca}\nModelo: {self.__modelo}\nVelocidad: {self._velocidad}\nCaballaje: {self._caballaje}\nPlazas: {self._plazas}" 
        return info
    
    # Método de clase para obtener el número de coches creados
    @classmethod
    def get_num_coches(cls):
        return cls.contador
    
# fin de la definción de la clase
```

Para hacer uso de esta clase podemos utilizar el siguiente código:
```py
# Importamos la clase Coche desde el archivo coche.py
from coche import Coche

# Creamos distintos objetos de la clase Coche con valores personalizados
coche1 = Coche("Amarillo", "Ferrari", "Aventador", 300, 500, 2)

print(coche1.color) # Acceso a un atributo público
print(coche1._velocidad) # Acceso a un atributo protegido

# Acceso a un atributo privado. Se produce un error, no se puede acceder a un atributo privado desde fuera de la clase
# print(coche1.__marca) 
  
print(coche1.getInfo())
```

El uso de atributos protegidos, no impide técnicamente el acceso desde fuera de la clase, pero indica al programador que el atributo no debería usarse directamente desde fuera de la clase ni desde código externo.

Es una convención, no una restricción estricta (como sí ocurre en lenguajes como Java o C++).

Por lo tanto, un atributo protegido puede ser accedido:
- Dentro de la propia clase.
- Dentro de las subclases (herencia).
- No se recomienda acceder a él desde fuera, pero es posible hacerlo (no hay error de compilación ni de ejecución).

## 4.1 Métodos Getters y Setters
Los getters y setters son métodos especiales que permiten obtener (getters) y asignar (setters) valores a los atributos o propiedades de un objeto.

Son muy utilizados en otros lenguajes para implementar el encapsulamiento. En Python no suelen utilizarse tanto, ya que las propiedades/métodos de un objeto son públicos.
