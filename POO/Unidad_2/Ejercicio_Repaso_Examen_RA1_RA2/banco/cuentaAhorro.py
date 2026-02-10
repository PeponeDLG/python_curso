from .cuenta import Cuenta

class CuentaAhorro(Cuenta):
    REINTEGRO_MIN = 100
    
    def __init__(self, numero_cuenta:str, titular:str, saldo:int, fecha_apertura:str):
        self.__tasa_interes_anual = float(0.02)
        super().__init__(numero_cuenta, titular, saldo, fecha_apertura)
    
    # Métodos
    def reintegro(self, cantidad:int):
        if cantidad < self.REINTEGRO_MIN:
            raise ValueError(f"La cantidad mínima del depósito es {self.REINTEGRO_MIN}€")
    
    def aplicar_interes(self):
        saldo = super().get_saldo
        saldo =  saldo * self.__tasa_interes_anual
        super().set_saldo(saldo)
    
    # Métodos de la clase abstracta
    def realizar_deposito(self, deposito:int):
        super().set_saldo(deposito)
    
    def retornar_saldo(self):
        super().set_saldo()

    