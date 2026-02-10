from abc import ABC, abstractmethod

class Embarcacion(ABC):
    # Constantes públicas de clase
    PATRON_POR_DEFECTO = "Sin patrón"
    RUMBO_POR_DEFECTO = "Sin rumbo"
    MIN_TRIPULANTES = 0                     # Número mínimo de tripulantes excluyendo al patrón

    # Atributos de clase
    __num_barcos_creados = 0
    __num_barcos_navegando = 0
    __tiempo_global_navegacion = 0          # Suma del tiempo de navegaciòn de todos los barcos

    def __init__(self, nombre:str, num_max_tripulantes:int):
        if not isinstance(nombre, str):
            raise ValueError("El nombre de la embarcación es obligatorio")
        elif nombre == "":
            raise ValueError("El nombre de la embarcación no puede estar vacío")
        elif not isinstance(num_max_tripulantes, int) or num_max_tripulantes < 0:
            raise ValueError("El número de tripulantes debe ser un entero positivo")
        elif num_max_tripulantes < Embarcacion.MIN_TRIPULANTES:
            raise ValueError(f"El número de tripulantes debe ser, como mínimo, {MIN_TRIPULANTES}.")

        # Atributos inmutables
        self._nombre = nombre
        self._num_max_tripulantes = num_max_tripulantes

        # Atributos que representan el estado del objeto en cada instante
        self._is_navegando = False

        # Atributos relacionados con la navegación
        self._velocidad = 0                 # Expresada en nudos
        self._patron = Embarcacion.PATRON_POR_DEFECTO
        self._rumbo = Embarcacion.RUMBO_POR_DEFECTO
        self._num_tripulantes = 0           # Sin contar al patrón
        self._tiempo_total_navegacion = 0   # Expresado en minutos

        # Incrementa el atributo de clase cada vez que se crea una instancia hija de Embarcacion
        Embarcacion.__num_barcos_creados += 1

    # *Método extra*: Formatea el tiempo de navegación en horas y minutos (hh:mm)
    def formatear_tiempo(self, minutos):
        horas_str = f"{int(minutos / 60)}"
        minutos_str = f"{minutos % 60}"
        # Añade un 0 delante de los minutos para formatear el tiempo correctamente
        if int(minutos_str) < 10:
            minutos_str = "0" + minutos_str
        horas_y_minutos = f"{horas_str}:{minutos_str}"

        return horas_y_minutos

    # Devuelve una cadena con el estado de la embarcación en un momento dado (se sobreescribirá)
    def __str__(self):
        navega = ""
        if self._is_navegando:
            navega = "Sí"
        else:
            navega = "No"
        
        # Cambia la cadena de salida según el velero esté navegando o no
        if self._is_navegando:
            return f"Nombre de la embarcación: {self._nombre}, Tripulación: {self._num_tripulantes}, Navegando: {navega}, a {self.__velocidad} nudos, Tiempo total de navegación del barco: {self.formatear_tiempo(self._tiempo_total_navegacion)} horas"
        else:
            return f"Nombre de la embarcación: {self._nombre}, Tripulación: {self._num_tripulantes}, Navegando: {navega}, Tiempo total de navegación del barco: {self.formatear_tiempo(self._tiempo_total_navegacion)} horas"
