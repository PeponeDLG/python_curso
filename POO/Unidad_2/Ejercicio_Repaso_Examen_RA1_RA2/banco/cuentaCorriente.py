from .cuenta import Cuenta

class CuentaCorriente(Cuenta):
        
    def __init__(self, numero_cuenta:str, titular:str, saldo:int, fecha_apertura:str):
        self.__tasa_interes_anual = float(0.02)
        self.__limite_descubierto = float(500.00)
        super().__init__(numero_cuenta, titular, saldo, fecha_apertura)
    
    # Métodos
    def reintegro(self, cantidad:int):
        saldo = super().get_saldo

        if cantidad > 0:
            saldo += cantidad * -1
        else:
            saldo += cantidad

        if saldo < (self.__limite_descubierto * -1) :
            raise ValueError(f"El descubierto no puede ser menor de -{self.__limite_descubierto}")
        
        super().set_reintegro(saldo)
    


    def aplicar_interes(self):
        saldo = super().get_saldo
        saldo =  saldo * self.__tasa_interes_anual
        super().set_saldo(saldo)
    
    # Métodos de la clase abstracta
    def realizar_deposito(self, deposito:int):
        super().set_saldo(deposito)
    
    def retornar_saldo(self):
        super().set_saldo()

    