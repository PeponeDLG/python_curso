class Vehículo:
    _marca
    _modelo
    _año

    def __init__(self, marca, modelo, año):
        self._marca = marca
        self._modelo = modelo
        self._año = año

    def arrancar(self):
        print("Arrancando ", self.modelo, "...")

    def detener(self):
        print("Deteniendo ", self._modelo, "...")


class Coche(Vehículo):
    __puertas

    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)

    super().arrancar() + " que es un coche"

    def __str__(self)
        

class Moto(Vehículo):
    __cilindrada

    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)

    super().arrancar() + " que es una moto"


class Camion(Vehículo):
    __capacidad_carga

    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)

    super().arrancar() + " que es un camion"
