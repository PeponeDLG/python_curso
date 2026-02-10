from iregateable import IRegateable
from embarcacion import Embarcacion

class Velero(Embarcacion):
    # Constantes públicas de clase
    MIN_MASTILES = 1
    MAX_MASTILES = 4
    MIN_VELOCIDAD_VELERO = 2
    MAX_VELOCIDAD_VELERO = 30

    # Atributos de clase
    __num_veleros_creados = 0

    # Constructor
    def __init__(self, nombre=None, num_max_tripulantes=None, num_mastiles=None):
        # Construcción sin parámetros. Establece valores por defecto
        if nombre == None and num_mastiles == None and num_max_tripulantes == None:
            self.__nombre = f"Velero {Velero.__num_veleros_creados + 1}"
            self.__num_mastiles = Velero.MIN_MASTILES
            self.__num_max_tripulantes = Embarcacion.MIN_TRIPULANTES
        else:   # Construcción con parámetros
            if not isinstance(num_mastiles, int):
                raise Exception("El número de mástiles debe ser un entero.")
            elif num_mastiles < Velero.MIN_MASTILES or num_mastiles > Velero.MAX_MASTILES:
                raise Exception(f"El número de mástiles debe estar entre {Velero.MIN_MASTILES} y {Velero.MAX_MASTILES}.")

            super().__init__(nombre, num_max_tripulantes)
            self.__num_mastiles = num_mastiles

        # Incrementa el atributo de clase cada vez que se crea una instancia de Velero
        Velero.__num_veleros_creados += 1

    def señalizar(self):    # TODO
        pass

    # Devuelve una cadena con el estado de la embarcación en un momento dado (se sobreescribirá)
    # Muestra una cadena con los datos del objeto
    def __str__(self):
        navega = ""
        if self._is_navegando:
            navega = "Sí"
        else:
            navega = "No"
        
        # Cambia la cadena de salida según el velero esté navegando o no
        if self._is_navegando:
            return f"{self._nombre}, Tripulación: {self.__num_tripulantes}, Navegando: {navega}, con el patrón {self.__nombre_patron} en {self.__rumbo} a {self.__velocidad} nudos, Tiempo total de navegación de la embarcación: {self.formatear_tiempo(self.__tiempo_total_navegacion)} horas, Número de mástiles: {self.__num_mastiles}"
            return f"{self._nombre}, Tripulación: {self.__num_tripulantes}, Navegando: {navega}, Tiempo total de navegación de la embarcación: {self.formatear_tiempo(self.__tiempo_total_navegacion)} horas, Número de mástiles: {self.__num_mastiles}"
