# Define la clase con su constructor y un método.
# Prueba la clase y sus métodos instanciando objetos y aplicándole el método mostrar_resultado()

class Partido:
    # Atributo de clase (contador de instancias)
    contador = 0

    # Método mágico constructor que sirve para instanciar objetos
    def __init__(self, equipo_local, equipo_visitante, puntos_local, puntos_visitante):
        # Atributos
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.puntos_local = puntos_local
        self.puntos_visitante = puntos_visitante

    # Cada vez que se crea un coche, el contador de la clase aumenta en 1
        Partido.contador += 1

    # Método que devuelve el equipo ganador
    def mostrar_resultado(self):
        print(f"{self.equipo_local} {self.puntos_local} - {self.puntos_visitante} {self.equipo_visitante}")
        if self.puntos_local > self.puntos_visitante:
            print(f"Ganó {self.equipo_local}")
        elif self.puntos_local < self.puntos_visitante:
            print(f"Ganó {self.equipo_visitante}")
        else:
            print("Empate")
        print("-"*30)

    # Método de clase que muestra el número de objetos creados
    @classmethod
    def get_num_partidos(cls):
        return cls.contador

# Crea varias instancias de partidos de prueba
partido1 = Partido("Lakers", "Celtics", 102, 99)
partido2 = Partido("Warriors", "Bulls", 88, 95)
partido3 = Partido("Heat", "Spurs", 110, 110)

# Prueba el método mostrar_resultado()
partido1.mostrar_resultado()
partido2.mostrar_resultado()
partido3.mostrar_resultado()

# Prueba el método de clase para mostrar el número de instancias creadas
print(f"Se han creado {Partido.get_num_partidos()} partidos en total.")


