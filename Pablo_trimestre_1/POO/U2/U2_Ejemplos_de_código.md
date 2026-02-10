# UT2.- POO y Diseño modular
## Ejemplos de código
https://educacionadistancia.juntadeandalucia.es/centros/cordoba/pluginfile.php/457626/mod_resource/content/2/index.html?nav=false
---
### Composición o Delegación
```py
# Clase contenida
class Motor:
    def arrancar(self):
        print("El motor está arrancando...")

    def detener(self):
        print("El motor se ha detenido.")


# Clase contenedora
class Coche:
    def __init__(self):
        # El coche tiene un motor
        self.motor = Motor()

    # Delegamos en el motor la acción de arrancar
    def arrancar(self):
        print("El coche está intentando arrancar...")
        self.motor.arrancar()

    # Delegamos en el motor la acción de detener
    def detener(self):
        print("El coche está intentando detenerse...")
        self.motor.detener()


# Uso
mi_coche = Coche()
mi_coche.arrancar()   # El coche no arranca directamente, delega al motor
mi_coche.detener()
```

### Agregación
#### Clases
```py
# clase contenida
class Equipo:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

    def __str__(self):
        return f"{self.nombre} de {self.ciudad}"

    def __eq__(self, other):
        # dos equipos son iguales si tienen el mismo nombre y ciudad
        return self.nombre == other.nombre and self.ciudad == other.ciudad


# clase contenedora
class Campeonato:
    def __init__(self, nombre, anio, descripcion):
        self.nombre = nombre
        self.anio = anio
        self.descripcion = descripcion
        self.equipos = []

    def __str__(self):
        return f"Campeonato {self.nombre} ({self.anio}) - {self.descripcion}"

    def agregar_equipo(self, equipo):
        # comprobar si el equipo ya está en la lista
        # funciona al estar definido el método __eq__ en la clase Equipo
        if equipo in self.equipos:
            return False
        self.equipos.append(equipo)
        return True
```

#### Programa principal
```py
from campeonato import Campeonato, Equipo   # Importamos las clases desde el módulo clases.py


class Main:
    @staticmethod
    def main():

        # Crear un campeonato
        liga = Campeonato('Liga', 2021, 'Campeonato de fútbol')

        # Crear equipos
        madrid = Equipo('Real Madrid', 'Madrid')
        betis = Equipo('Betis', 'Sevilla')

        # Agregar equipos al campeonato
        liga.agregar_equipo(madrid)
        liga.agregar_equipo(betis)
        liga.agregar_equipo(Equipo('Athletic', 'Bilbao'))
        liga.agregar_equipo(Equipo('Athletic', 'Bilbao'))  # Repetido → no se añadirá

        # Mostrar los equipos inscritos
        for equipo in liga.equipos:
            print(equipo)

if __name__== "__main__":
    Main.main()
```


```py

```
