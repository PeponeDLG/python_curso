from abc import ABC, abstractmethod
import datetime as dtm

class Cuenta(ABC):
    __numeros_cuenta_total:list[str] = []
    
    def __init__(self, numero_cuenta:str, titular:str, saldo:int, fecha_apertura:str):
        try:
            if self.none_vacio(numero_cuenta) or self.none_vacio(titular) or self.none_vacio(fecha_apertura):
                raise Exception("Debe completar todos los campos")
            elif saldo < 0:
                raise Exception("No puede abrir una cuenta con un saldo negativo")
            else:
                if self.validar_fecha(fecha_apertura) != True:
                    raise Exception("El formato de la fecha no es correcto. Debe ser DD-MM-AAAA")
                
                if numero_cuenta in Cuenta.__numeros_cuenta_total:
                    raise Exception(f"El número de cuenta {numero_cuenta} ya existe. Introduzca uno nuevo")
                    
                Cuenta.__numeros_cuenta_total.append(numero_cuenta)
                self.__numero_cuenta = numero_cuenta
                self.__titular = titular
                self.__saldo = saldo                    
                self.__fecha_apertura = fecha_apertura
                
        except Exception as e:
            print(f"Ha habido algún problema con los datos de inicio:\n {e}")
    
    # VALIDACIONES
    def validar_fecha(self, fecha:str) -> bool:
        try:
            fecha_aux = dtm.datetime.strptime(fecha,"%d-%m-%Y")
            
            return True
        except Exception as e:
            return False
    
    def none_vacio(self, cadena):
        return len(cadena.strip()) == 0

    @abstractmethod
    def realizar_deposito(self, ingreso):
        pass
    
    @abstractmethod
    def retornar_saldo(self):
        pass
    
        
    # SOBRECARGA DE MÉTODOS 
    def __str__(self):
        return f"IBAN: {self.__numero_cuenta} - Titular: {self.__titular} - Saldo: {self.__saldo}"
        
    
    def __ne__(self, numero_cuenta:str) -> bool:
        
        if str.isspace(numero_cuenta):
            raise ValueError("El número de cuenta no puede estar vacío")
        elif numero_cuenta == self.__numero_cuenta:
            return False
            
        return True
    
    # Setter
    def set_saldo(self, deposito:int):
        if deposito <= 0:
            raise ValueError("El valor del depósito debe ser mayor que 0")
        else:
            self.__saldo += deposito
    
    def set_reintegro(self, cantidad):
        self.__saldo = cantidad

    # Getter
    @property
    def get_saldo(self) -> int:
        return self.__saldo