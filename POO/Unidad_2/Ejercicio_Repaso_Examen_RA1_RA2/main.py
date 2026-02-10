import os
import datetime as dtm
from banco.cuentaAhorro import CuentaAhorro
from banco.cuentaCorriente import CuentaCorriente

class Main:
    @staticmethod
    def main():
        try:
            os.system('clear' if os.name == 'posix' else 'cls')
                                    
            cuenta1 = CuentaAhorro("1","Pepe",1000,"15-12-2025")
            
            cuenta2:CuentaAhorro
            
            if cuenta1 != "2":
                cuenta2 = CuentaAhorro("2","Carlos",500,"16-12-2025")
            
            print(cuenta1.__str__())
            print(cuenta2.__str__())
            
            # Main.pausa()
            
            cuenta1.realizar_deposito(20)
            print("El saldo de cuenta1 es: ",cuenta1.get_saldo)
            
            cuenta1.reintegro(100)
            print(cuenta1.get_saldo)
            cuenta1.aplicar_interes()
            print(cuenta1.get_saldo)
            
            Main.pausa()

            print("Cuenta corriente")
            
            cuentaC1 = CuentaCorriente("3","Pepe",1000,"15-12-2025")
            print(cuentaC1.get_saldo)
            cuentaC1.reintegro(1500)
            print(cuentaC1.get_saldo)
            
        except Exception as e:
            print("Error: ", e)            

    @staticmethod
    def pausa():
        input("Pulse Enter para continuar...")            
        os.system('clear' if os.name == 'posix' else 'cls')

if __name__ == "__main__":
    Main.main()