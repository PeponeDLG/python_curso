import ejercicio1 as ej1
import ejercicio2 as ej2
import ejercicio3 as ej3
import ejercicio4 as ej4
import GestionArchivo as ej5
import os

class Main:
    @staticmethod
    def main():
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("EJERCICIO 1")
        print("-----------\n")
        ej1.Ejercicio1.ejercicio()
        Main.siguiente()

        print("EJERCICIO 2")
        print("-----------\n")
        ej2.Ejercicio2.ejercicio()
        Main.siguiente()

        print("EJERCICIO 3")
        print("-----------\n")
        ej3.Ejercicio3.ejercicio()
        Main.siguiente()

        print("EJERCICIO 4")
        print("-----------\n")
        ej4.Ejercicio4.ejercicio()
        Main.siguiente()

        print("EJERCICIO 5")
        print("-----------\n")
        ruta = os.path.join(os.path.dirname(__file__),"operaciones.txt")
        cadena = "S11_1111"
        print("Busca ",cadena,": ",ej5.GestionArchivo.buscar(ruta,cadena))
        print("\nCuenta ",cadena,": ",ej5.GestionArchivo.contar(ruta,cadena))
        lista = ej5.GestionArchivo.mostrar(ruta,cadena)
        print("\nMuestra:")
        
        for linea in lista:
            print(str.strip(linea))
        
           
    def siguiente():
        input("pulse una enter para continuar...")
        os.system('clear' if os.name == 'posix' else 'cls')        

if __name__=="__main__":
    Main.main()
