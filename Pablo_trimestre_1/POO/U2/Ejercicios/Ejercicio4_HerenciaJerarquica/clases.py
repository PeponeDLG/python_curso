# Clase padre o superclase
class Vehiculo:
    def __init__(self, marca:str, modelo:str, año:int):
        self._marca = marca
        self._modelo = modelo
        self._año = año

    def __str__(self):
        return f"{self._marca} {self._modelo} - {self._año}"

    def arrancar(self):
        return "Arrancando..."

    def detener(self):
        return "Detenido"

# Clases hija o sublases
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.__puertas = puertas

    def __str__(self):
        return super().__str__() + f" - {self.__puertas} puertas"

    def arrancar(self):
        return "El coche está arrancando"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.__cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f" - {self.__cilindrada}cc"

    def arrancar(self):
        return "La moto está arrancando"

class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.__capacidad_carga = capacidad_carga

    def __str__(self):
        return super().__str__() + f" - Hasta {self.__capacidad_carga} toneladas"

    def arrancar(self):
        return "El camión está arrancando"
