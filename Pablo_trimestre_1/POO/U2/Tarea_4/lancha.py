from embarcacion import Embarcacion

class Lancha(Embarcacion):
    # Constantes públicas de clase
    MIN_MOTORES = 1
    MAX_MOTORES = 2
    MIN_COMBUSTIBLE = 8         # Expresado en litros
    MAX_COMBUSTIBLE = 50        # Expresado en litros
    FACTOR_COMBUSTIBLE = 0.026
    MIN_VELOCIDAD_LANCHA = 1    # Expresado en nudos
    MAX_VELOCIDAD_LANCHA = 50   # Expresado en nudos

    # Atributo de clase
    __num_lanchas_creadas = 0

    def __init__(self, nombre=None, num_max_tripulantes=None, num_motores=None, combustible=None):
        if num_motores < Lancha.MIN_MOTORES or num_motores > Lancha.MAX_MOTORES:
            raise Exception(f"El número de motores debe estar entre {Lancha.MIN_MOTORES} y {Lancha.MAX_MOTORES}.")
        elif combustible < Lancha.MIN_COMBUSTIBLE or combustible > Lancha.MAX_COMBUSTIBLE:
            raise Exception(f"El nivel de combustible debe estar entre {Lancha.MIN_COMBUSTIBLE} y {Lancha.MAX_COMBUSTIBLE}.")

        super().__init__(nombre, num_max_tripulantes)
        self.__num_motores = num_motores
        self.__combustible = combustible

    # Muestra la información de una instancia de Lancha
    def __str__(self):
        return f"{super().__str__()}, Número de motores: {self.__num_motores}, Nivel de combustible: {self.__combustible}"
