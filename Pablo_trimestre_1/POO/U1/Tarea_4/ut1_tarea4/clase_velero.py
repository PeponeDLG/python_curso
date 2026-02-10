class Velero:
    # Constantes públicas de clase
    MIN_MASTILES = 1
    MAX_MASTILES = 4
    MIN_VELOCIDAD = 2
    MAX_VELOCIDAD = 30
    PATRON_POR_DEFECTO = "Sin patrón"
    RUMBO_POR_DEFECTO = "Sin rumbo"
    MIN_TRIPULANTES = 0 # Número mínimo de tripulantes excluyendo al patrón

    # Atributos de clase
    __num_barcos_creados = 0
    __num_barcos_navegando = 0
    __tiempo_global_navegacion = 0  # Suma del tiempo de navegaciòn de todos los barcos

    # Constructor
    def __init__(self, nombre=None, num_mastiles=None, num_max_tripulantes=None):
        # Construcción sin parámetros. Establece valores por defecto
        if nombre == None and num_mastiles == None and num_max_tripulantes == None:
            self.__nombre = f"Velero {Velero.__num_barcos_creados + 1}"
            self.__num_mastiles = Velero.MIN_MASTILES
            self.__num_max_tripulantes = Velero.MIN_TRIPULANTES
        else:   # Construcción con parámetros
            if nombre == "":
                raise Exception("El nombre del velero no puede estar vacío.")
            elif not isinstance(nombre, str):
                raise Exception("El nombre del velero debe de ser una cadena de texto.")
            elif not isinstance(num_mastiles, int):
                raise Exception("El número de mástiles debe ser un entero.")
            elif not isinstance(num_max_tripulantes, int):
                raise Exception("El número de tripulantes debe ser un entero.")
            elif num_mastiles < Velero.MIN_MASTILES or num_mastiles > Velero.MAX_MASTILES:
                raise Exception(f"El número de mástiles debe estar entre {Velero.MIN_MASTILES} y {Velero.MAX_MASTILES}.")
            elif num_max_tripulantes < Velero.MIN_TRIPULANTES:
                raise Exception(f"El número máximo de tripulantes debe ser como mínimo {Velero.MIN_TRIPULANTES}.")
            
            # Atributos inmutables con valores definidos al instanciar el objeto
            self.__nombre = nombre
            self.__num_mastiles = num_mastiles
            self.__num_max_tripulantes = num_max_tripulantes

        # Atributos que representan el estado del objeto en cada instante
        self.__esta_navegando = False
        self.__tiempo_total_navegacion = 0  # Expresado en minutos

        # Atributos relacionados con la navegación
        self.__velocidad = 0    # Expresada en nudos
        self.__nombre_patron = Velero.PATRON_POR_DEFECTO
        self.__rumbo = Velero.RUMBO_POR_DEFECTO
        self.__num_tripulantes = 0

        # Incrementa el atributo de clase cada vez que se crea una instancia de Velero
        Velero.__num_barcos_creados += 1

    # Getters
    @property
    def get_nombre_barco(self):
        return self.__nombre

    @property
    def get_num_mastiles(self):
        return self.__num_mastiles

    @property
    def get_num_max_tripulantes(self):
        return self.__num_max_tripulantes
    
    @property
    def is_navegando(self):
        return self.__esta_navegando

    @property
    def get_tiempo_total_navegacion_barco(self):
        return self.__tiempo_total_navegacion

    @property
    def get_velocidad(self):
        return self.__velocidad

    @property
    def get_rumbo(self):
        return self.__rumbo

    @property
    def get_tripulacion(self):
        return self.__num_tripulantes

    # Métodos para consultar los atributos de clase
    @classmethod
    def get_num_barcos(cls):
        return cls.__num_barcos_creados

    @classmethod
    def get_num_barcos_navegando(cls):
        return cls.__num_barcos_navegando

    @classmethod
    def get_tiempo_global_navegacion(cls):
        return cls.__tiempo_global_navegacion

    # Crea y devuelve una lista de objetos Velero construidos con parámetros por defecto
    @classmethod
    def crear_lista_velero(cls, num_barcos):
        lista = []
        for i in range(num_barcos):
            if num_barcos not in range(1, 10):
                raise Exception("Número de barcos incorrecto. Debe de ser mayor o igual que 1 y menor o igual que 10.")
            lista.append(Velero())

        return lista

    # Inicia la navegación de un velero
    def iniciar_navegacion(self, velocidad, rumbo, nombre_patron, num_tripulantes):
        if velocidad not in range(Velero.MIN_VELOCIDAD, Velero.MAX_VELOCIDAD):
            if velocidad < Velero.MIN_VELOCIDAD:
                raise Exception(f"La velocidad es inferior a {Velero.MIN_VELOCIDAD}.")
            else:
                raise Exception(f"La velocidad es superior a {Velero.MAX_VELOCIDAD}.")
        elif self.__esta_navegando:
            raise Exception(f"El velero {self.__nombre} ya está navegando y se encuentra fuera del puerto.")
        elif rumbo == "":
            raise Exception("El rumbo no puede estar vacío, debes indicar el rumbo para iniciar la navegación.")
        elif nombre_patron == "":
            raise Exception("El patrón del barco no puede estar vacío, se necesita un patrón para iniciar la navegación.")
        elif num_tripulantes not in range(Velero.MIN_TRIPULANTES, self.__num_max_tripulantes):
            raise Exception(f"El número de tripulantes debe estar entre {Velero.MIN_TRIPULANTES} y {self.__num_max_tripulantes}.")

        self.__esta_navegando = True
        self.__velocidad = velocidad
        self.__rumbo = rumbo
        self.__nombre_patron = nombre_patron
        self.__num_tripulantes = num_tripulantes

        # Incrementa el atributo de clase cada vez que un velero comienza a navegar
        Velero.__num_barcos_navegando += 1

    # Finaliza la navegación
    def parar_navegacion(self, tiempo_navegando):
        if not self.__esta_navegando:
            raise Exception(f"El velero {self.__nombre} no está navegando.")
        elif tiempo_navegando < 1:
            raise Exception("Tiempo navegando incorrecto, debe ser mayor que cero.")

        self.__esta_navegando = False
        self.__tiempo_total_navegacion += tiempo_navegando

        # Suma el tiempo de navegación del velero al global
        Velero.__tiempo_global_navegacion += tiempo_navegando

        # Decrementa el atributo de clase cada vez que un velero deja de navegar
        Velero.__num_barcos_navegando -= 1

    # Cambia el rumbo
    def set_rumbo(self, rumbo):
        if not self.__esta_navegando:
            raise Exception(f"El velero {self.__nombre} no está navegando, no se puede cambiar el rumbo.")
        elif rumbo != "ceñida" and rumbo != "empopada":
            raise Exception("El rumbo no es correcto, debes indicar el rumbo (ceñida o empopada) para poder modificarlo.")
        elif rumbo == self.__rumbo:
            raise Exception(f"El velero {self.__nombre} ya está navegando con ese rumbo ({self.__rumbo}, debes indicar un rumbo distinto para poder modificarlo.)")

        self.__rumbo = rumbo

    # Inicia una regata
    def iniciar_regata(self, oponente):
        if not self.__esta_navegando:
            raise Exception(f"No se puede iniciar la regata, el barco {self.__nombre} no está navegando")
        elif not oponente.__esta_navegando:
            raise Exception(f"No se puede iniciar la regata, el barco {oponente.__nombre} no está navegando")
        elif self.__rumbo != oponente.__rumbo:
            raise Exception(f"No se puede iniciar la regata, los barcos {self.__nombre} y {oponente.__nombre} deben navegar con el mismo rumbo.")
        elif self.__num_mastiles != oponente.__num_mastiles:
            raise Exception(F"No se puede iniciar la regata, los barcos {self.__nombre} y {oponente.__nombre} no tienen el mismo número de mástiles.")
        elif oponente is None:
            raise Exception("El barco con el que se intenta regatear no existe.")

        if self.__velocidad > oponente.__velocidad:
            return f"El barco {self.__nombre} ha llegado antes a la línea de llegada."
        elif oponente.__velocidad > self.__velocidad:
            return f"El barco {oponente.__nombre} ha llegado antes a la línea de llegada."
        else:
            return f"Los barcos {self.__nombre} y {oponente.__nombre} han llegado a la vez a la línea de llegada."

    # *Método extra*: Formatea el tiempo de navegación en horas y minutos (hh:mm)
    def formatear_tiempo(self, minutos):
        horas_str = f"{int(minutos / 60)}"
        minutos_str = f"{minutos % 60}"
        # Añade un 0 delante de los minutos para formatear el tiempo correctamente
        if int(minutos_str) < 10:
            minutos_str = "0" + minutos_str
        horas_y_minutos = f"{horas_str}:{minutos_str}"

        return horas_y_minutos

    # Muestra una cadena con los datos del objeto
    def __str__(self):
        navega = ""
        if self.__esta_navegando:
            navega = "Sí"
        else:
            navega = "No"
        
        # Cambia la cadena de salida según el velero esté navegando o no
        if self.__esta_navegando:
            return f"Nombre del barco: {self.__nombre}, Número de mástiles: {self.__num_mastiles}, Tripulación: {self.__num_tripulantes}, Navegando: {navega}, con el patrón {self.__nombre_patron} en {self.__rumbo} a {self.__velocidad} nudos, Tiempo total de navegación del barco: {self.formatear_tiempo(self.__tiempo_total_navegacion)} horas"
        else:
            return f"Nombre del barco: {self.__nombre}, Número de mástiles: {self.__num_mastiles}, Tripulación: {self.__num_tripulantes}, Navegando: {navega}, Tiempo total de navegación del barco: {self.formatear_tiempo(self.__tiempo_total_navegacion)} horas"