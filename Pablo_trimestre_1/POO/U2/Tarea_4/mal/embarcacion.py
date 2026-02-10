from abc import ABC, abstractmethod
from inavegable import INavegable

class Embarcacion(ABC):
    # Constantes públicas de clase
    PATRON_POR_DEFECTO = "Sin patrón"
    RUMBO_POR_DEFECTO = "Sin rumbo"
    MIN_TRIPULANTES = 0 # Número mínimo de tripulantes excluyendo al patrón

    # Atributos de clase
    __num_embarcaciones_creadas = 0
    __num_embarcaciones_navegando = 0
    __tiempo_global_navegacion = 0  # Suma del tiempo de navegaciòn de todas las embarcaciones

    def __init__(self, nombre:str, num_max_tripulantes:int): # TODO verificar que las validaciones son correctas (apuntes 1.1.2)
        if not isinstance(nombre, str):
            raise ValueError("El nombre de la embarcación es obligatorio")
        elif nombre == "":
            raise ValueError("El nombre de la embarcación no puede estar vacío")
        elif num_max_tripulantes < Embarcacion.MIN_TRIPULANTES:
                raise Exception(f"El número máximo de tripulantes debe ser como mínimo {Embarcacion.MIN_TRIPULANTES}.")

        # Atributos inmutables con valores definidos al instanciar el objeto
        self._nombre = nombre
        self._num_max_tripulantes = num_max_tripulantes

        # Atributos que representan el estado del objeto en cada instante
        self._is_navegando = False
        self._tiempo_total_navegacion = 0  # Expresado en minutos

        # Atributos relacionados con la navegación
        self._velocidad = 0    # Expresada en nudos
        self._nombre_patron = Embarcacion.PATRON_POR_DEFECTO
        self._rumbo = Embarcacion.RUMBO_POR_DEFECTO
        self._num_tripulantes = 0

        # Incrementa el atributo de clase cada vez que se crea una instancia hija de Embarcacion
        Embarcacion.__num_embarcaciones_creadas += 1

    # Getters de instancia
    @property
    def get_nombre_barco(self):
        return self.__nombre

    @property
    def get_num_max_tripulantes(self):
        return self.__num_max_tripulantes

    @property
    def is_navegando(self):
        return self._is_navegando

    @property
    def get_velocidad(self):
        return self.__velocidad

    @property
    def get_rumbo(self):
        return self.__rumbo

    @property
    def get_patron(self):
        return self.__nombre_patron

    @property
    def get_tripulacion(self):
        return self.__num_tripulantes

    @property
    def get_tiempo_total_navegacion(self):
        return self.__tiempo_total_navegacion

    # Getters de clase
    @classmethod
    def get_num_barcos(cls):
        return cls.__num_embarcaciones_creadas

    @classmethod
    def get_num_barcos_navegando(cls):
        return cls.__num_embarcaciones_navegando

    @classmethod
    def get_tiempo_total_navegancion_acumulado(cls):
        return cls.__tiempo_global_navegacion

    # Métodos
    # Cambia el rumbo
    def set_rumbo(self, rumbo):
        if not self._is_navegando:
            raise Exception(f"La embarcación {self.__nombre} no está navegando, no se puede cambiar el rumbo.")
        elif rumbo != "ceñida" and rumbo != "empopada":
            raise Exception("El rumbo no es correcto, debes indicar el rumbo (ceñida o empopada) para poder modificarlo.")
        elif rumbo == self.__rumbo:
            raise Exception(f"La embarcación {self.__nombre} ya está navegando con ese rumbo ({self.__rumbo}, debes indicar un rumbo distinto para poder modificarlo.)")

        self.__rumbo = rumbo

    # Inicia la navegación de una embarcación
    def iniciar_navegacion(self, velocidad, rumbo, nombre_patron, num_tripulantes):
        if velocidad not in range(Embarcacion.MIN_VELOCIDAD, Embarcacion.MAX_VELOCIDAD):
            if velocidad < Embarcacion.MIN_VELOCIDAD:
                raise Exception(f"La velocidad es inferior a {Embarcacion.MIN_VELOCIDAD}.")
            else:
                raise Exception(f"La velocidad es superior a {Embarcacion.MAX_VELOCIDAD}.")
        elif self._is_navegando:
            raise Exception(f"La embarcación {self.__nombre} ya está navegando y se encuentra fuera del puerto.")
        elif rumbo == "":
            raise Exception("El rumbo no puede estar vacío, debes indicar el rumbo para iniciar la navegación.")
        elif nombre_patron == "":
            raise Exception("El patrón de la embarcación no puede estar vacío, se necesita un patrón para iniciar la navegación.")
        elif num_tripulantes not in range(Embarcacion.MIN_TRIPULANTES, self.__num_max_tripulantes):
            raise Exception(f"El número de tripulantes debe estar entre {Embarcacion.MIN_TRIPULANTES} y {self.__num_max_tripulantes}.")

        self._is_navegando = True
        self.__velocidad = velocidad
        self.__rumbo = rumbo
        self.__nombre_patron = nombre_patron
        self.__num_tripulantes = num_tripulantes

        # Incrementa el atributo de clase cada vez que una embarcación comienza a navegar
        Embarcacion._num_barcos_navegando += 1

    # Finaliza la navegación
    def parar_navegacion(self, tiempo_navegando):
        if not self._is_navegando:
            raise Exception(f"La embarcación {self.__nombre} no está navegando.")
        elif tiempo_navegando < 1:
            raise Exception("Tiempo navegando incorrecto, debe ser mayor que cero.")

        self._is_navegando = False
        self.__tiempo_total_navegacion += tiempo_navegando

        # Suma el tiempo de navegación de la embarcación al global
        Embarcacion.__tiempo_global_navegacion += tiempo_navegando

        # Decrementa el atributo de clase cada vez que una embarcación deja de navegar
        Embarcacion._num_barcos_navegando -= 1

    # Método abstracto para indicar la señalización de las embarcaciones
    @abstractmethod
    def señalizar(self):
        pass

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
    # Muestra una cadena con los datos del objeto
    def __str__(self):
        navega = ""
        if self._is_navegando:
            navega = "Sí"
        else:
            navega = "No"
        
        # Cambia la cadena de salida según el velero esté navegando o no
        if self._is_navegando:
            return f"Nombre de la embarcación: {self._nombre}, Tripulación: {self.__num_tripulantes}, Navegando: {navega}, con el patrón {self.__nombre_patron} en {self.__rumbo} a {self.__velocidad} nudos, Tiempo total de navegación del barco: {self.formatear_tiempo(self.__tiempo_total_navegacion)} horas"
        else:
            return f"Nombre de la embarcación: {self._nombre}, Tripulación: {self.__num_tripulantes}, Navegando: {navega}, Tiempo total de navegación del barco: {self.formatear_tiempo(self.__tiempo_total_navegacion)} horas"
