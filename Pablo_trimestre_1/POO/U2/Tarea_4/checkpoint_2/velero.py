from embarcacion import Embarcacion

class Velero(Embarcacion):
    # Constantes públicas de clase
    MIN_MASTILES = 1
    MAX_MASTILES = 4
    MIN_VELOCIDAD_VELERO = 2    # Expresado en nudos
    MAX_VELOCIDAD_VELERO = 30   # Expresado en nudos

    # Atributo de clase
    __num_veleros_creados = 0

    def __init__(self=None, nombre=None, num_max_tripulantes=None, num_mastiles=None):
        if num_mastiles < Velero.MIN_MASTILES or num_mastiles > Velero.MAX_MASTILES:
            raise Exception(f"El número de mástiles debe estar entre {Velero.MIN_MASTILES} y {Velero.MAX_MASTILES}.")
            
        super().__init__(nombre, num_max_tripulantes)
        self.__num_mastiles = num_mastiles

        # Incrementa el atributo de clase cada vez que se crea una instancia de Velero
        Velero.__num_veleros_creados += 1

    # Getters para los atributos de clase y de instancia
    @classmethod
    def num_veleros_creados(cls):
        return cls.__num_veleros_creados

    @property
    def num_mastiles(self):
        return self.__num_mastiles

    # Setter para cambiar el rumbo
    @Embarcacion.rumbo.setter
    def rumbo(self, rumbo):
        pass

    # Muestra la información de una instancia de Velero
    def __str__(self):
        return f"{super().__str__()}, Número de mástiles: {self.__num_mastiles}"
    