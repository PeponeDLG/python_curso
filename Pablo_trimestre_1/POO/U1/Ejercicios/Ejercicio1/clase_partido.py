# Define la clase con su constructor y un método.
# Prueba la clase y sus métodos instanciando objetos y aplicándole el método mostrar_resultado()

class Partido:
    # Método mágico constructor que sirve para instanciar objetos
    def __init__(self, equipo_local, equipo_visitante, puntos_local, puntos_visitante):
        # Atributos
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.puntos_local = puntos_local
        self.puntos_visitante = puntos_visitante

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

# Crea varias instancias de partidos de prueba
partido1 = Partido("Lakers", "Celtics", 102, 99)
partido2 = Partido("Warriors", "Bulls", 88, 95)
partido3 = Partido("Heat", "Spurs", 110, 110)

# Prueba el método mostrar_resultado()
partido1.mostrar_resultado()
partido2.mostrar_resultado()
partido3.mostrar_resultado()
