from embarcacion import Embarcacion

class Velero(Embarcacion):
    # Constantes públicas de clase
    MIN_MASTILES = 1
    MAX_MASTILES = 4
    MIN_VELOCIDAD_VELERO = 2    # Expresado en nudos
    MAX_VELOCIDAD_VELERO = 30   # Expresado en nudos

    # Atributo de clase
    __num_veleros_creados = 0

    def __init__(self, nombre, num_max_tripulantes, num_mastiles):
        super().__init__(nombre, num_max_tripulantes)
        self.__num_mastiles = num_mastiles

        # Incrementa el atributo de clase cada vez que se crea una instancia de Velero
        Velero.__num_veleros_creados += 1

    def __str__(self):
        return f"{super().__str__()}, Número de mástiles: {self.__num_mastiles}"
    