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

    # Inicia la navegación de un velero
    def iniciar_navegacion(self, velocidad, rumbo, nombre_patron, num_tripulantes):
        if velocidad not in range(Velero.MIN_VELOCIDAD_VELERO, Velero.MAX_VELOCIDAD_VELERO):
            if velocidad < Velero.MIN_VELOCIDAD_VELERO:
                raise Exception(f"La velocidad es inferior a {Velero.MIN_VELOCIDAD_VELERO}.")
            else:
                raise Exception(f"La velocidad es superior a {Velero.MAX_VELOCIDAD_VELERO}.")
        elif self._is_navegando:
            raise Exception(f"El velero {self._nombre} ya está navegando y se encuentra fuera del puerto.")
        elif rumbo == "":
            raise Exception("El rumbo no puede estar vacío, debes indicar el rumbo para iniciar la navegación.")
        elif nombre_patron == "":
            raise Exception("El patrón del barco no puede estar vacío, se necesita un patrón para iniciar la navegación.")
        elif num_tripulantes not in range(Velero.MIN_TRIPULANTES, self._num_max_tripulantes):
            raise Exception(f"El número de tripulantes debe estar entre {Velero.MIN_TRIPULANTES} y {self._num_max_tripulantes}.")

        self._is_navegando = True
        self._velocidad = velocidad
        self._rumbo = rumbo
        self._nombre_patron = nombre_patron
        self._num_tripulantes = num_tripulantes

        # Incrementa el atributo de clase cada vez que un velero comienza a navegar
        super().add_navegando()

    # Finaliza la navegación
    def parar_navegacion(self, tiempo_navegando):
        if not self._is_navegando:
            raise Exception(f"El velero {self._nombre} no está navegando.")
        elif tiempo_navegando < 1:
            raise Exception("Tiempo navegando incorrecto, debe ser mayor que cero.")

        self._is_navegando = False
        super().add_tiempo_navegacion(tiempo_navegando)

        # Suma el tiempo de navegación del velero al global
        super().add_tiempo_global_navegacion(tiempo_navegando)

        # Decrementa el atributo de clase cada vez que un velero deja de navegar
        super().minus_navegando()

    # Inicia una regata
    def iniciar_regata(self, oponente):
        if not self._is_navegando:
            raise Exception(f"No se puede iniciar la regata, el barco {self._nombre} no está navegando")
        elif not oponente._is_navegando:
            raise Exception(f"No se puede iniciar la regata, el barco {oponente._nombre} no está navegando")
        elif self._rumbo != oponente._rumbo:
            raise Exception(f"No se puede iniciar la regata, los barcos {self._nombre} y {oponente._nombre} deben navegar con el mismo rumbo.")
        elif self.__num_mastiles != oponente.__num_mastiles:
            raise Exception(F"No se puede iniciar la regata, los barcos {self._nombre} y {oponente._nombre} no tienen el mismo número de mástiles.")
        elif oponente is None:
            raise Exception("El barco con el que se intenta regatear no existe.")

        if self._velocidad > oponente._velocidad:
            return f"El barco {self._nombre} ha llegado antes a la línea de llegada."
        elif oponente._velocidad > self._velocidad:
            return f"El barco {oponente._nombre} ha llegado antes a la línea de llegada."
        else:
            return f"Los barcos {self._nombre} y {oponente._nombre} han llegado a la vez a la línea de llegada."

    # Cambia el rumbo
    def set_rumbo(self, rumbo):
        super().set_rumbo(rumbo)
        if rumbo == None:
            raise Exception("El rumbo no puede ser nulo, debes indicar el rumbo (ceñida o empopada) para poder modificarlo.")
        elif rumbo != "ceñida" and rumbo != "empopada":
            raise Exception("El rumbo no es correcto, debes indicar el rumbo (ceñida o empopada) para poder modificarlo.")

        self._rumbo = rumbo

    # Muestra la información de una instancia de Velero
    def __str__(self):
        return f"{super().__str__()}, Número de mástiles: {self.__num_mastiles}"
    