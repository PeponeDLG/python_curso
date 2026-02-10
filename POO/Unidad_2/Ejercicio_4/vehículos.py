class Vehículo:
    _marca:str
    _modelo:str
    _año:int

    def __init__(self, marca, modelo, año):
        self._marca = marca
        self._modelo = modelo
        self._año = año

    def arrancar(self):
        print("Arrancando ", self._modelo, "...")

    def detener(self):
        print("Deteniendo ", self._modelo, "...")


class Coche(Vehículo):
    __puertas=5

    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)

    def arrancar(self):
        super().arrancar() , " que es un coche"

    def __str__(self):
        return f"{super().__str__}\nNº Puertas: {self.__puertas}"


class Moto(Vehículo):
    __cilindrada = "650cc"

    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)

    def arrancar(self):
        super().arrancar() , " que es una moto"

    def __str__(self):        
        return f"{super().__str__}\nCilindrada: {self.__cilindrada}"
        

class Camion(Vehículo):
    __capacidad_carga="500kg"

    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)

    def arrancar(self):
        super().arrancar() , " que es un camion"


    def __str__(self):
        return f"{super().__str__}\nCapacidad: {self.__capacidad_carga}"
