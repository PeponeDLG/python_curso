# Define la clase con su constructor y un método.
# Prueba la clase y sus métodos instanciando objetos y aplicándole el método is_longer_than_2h()

class Pelicula:
    # Método mágico constructor que sirve para instanciar objetos
    def __init__(self, titulo, director, duracion_minutos):
        # Atributos
        self.titulo = titulo
        self.director = director
        self.duracion_minutos = duracion_minutos

    # Método que devuelve si la película dura más de 2 horas
    def is_longer_than_2h(self):
        if self.duracion_minutos > 120:
            print(f"La película '{self.titulo}' dura más de 2 horas.")
        elif self.duracion_minutos < 120:
            print(f"La película '{self.titulo}' dura menos de 2 horas.")
        else:
            print(f"La película '{self.titulo}' dura exactamente 2 horas.")
        print("-"*30)

# Crea varias instancias de partidos de prueba
pelicula_1 = Pelicula("El Señor de Los Anillos", "Peter Jackson", 10000)
pelicula_2 = Pelicula("La Vida de Bryan", "Terry Gilliam", 100)
pelicula_3 = Pelicula("Matrix", "Hermanas Wachowski", 120)

# Prueba el método is_longer_than_2h()
pelicula_1.is_longer_than_2h()
pelicula_2.is_longer_than_2h()
pelicula_3.is_longer_than_2h()
