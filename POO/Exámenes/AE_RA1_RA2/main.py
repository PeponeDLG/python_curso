import os
from partido_futbol import Partido_Futbol 
from partido_baloncesto import Partido_Baloncesto
from partido_tenis import Partido_Tenis

class Main:
    @staticmethod
    def main():

            os.system('clear' if os.name == 'posix' else 'cls')

            futbol1 = Partido_Futbol("Córdoba", "Sevilla", "01-13-2025",1,) # Prueba fecha erronea
            futbol1 = Partido_Futbol("Córdoba", "Sevilla", "01-13-2025",-1,) # Prueba goles negativos

            futbol1 = Partido_Futbol("Córdoba", "Sevilla", "01-12-2025",1,)
            futbol2 = Partido_Futbol("Atleti", "Barcelona", "01-12-2025",1,)

            print(futbol1.ganador())
            print(futbol1.resultado())
            print(futbol1.representacion())

            print(futbol2.ganador())
            print(futbol2.resultado())
            print(futbol2.representacion())

            futbol1.comprobar_partidos("Atleti", "Barcelona", "01-12-2025") # Comprobación de partido

            Main.pausa()

            baloncesto1 = Partido_Baloncesto("Málaga", "Estudiantes", "01-12-2025",40,95)
            baloncesto2 = Partido_Baloncesto("Madrid", "Barceloona", "01-12-2025",0,50)
            
            baloncesto1.comprobar_partidos("Málaga", "Estudiantes", "01-12-2025")
            print(baloncesto1.ganador())
            print(baloncesto1.resultado())
            print(baloncesto1.representacion())

            Main.pausa()

            tenis1 = Partido_Tenis("federe","nadal","03-12-2025","Rolan Garros",[5,6,5,6],[1,4,5]) # resultados distintos
            tenis2 = Partido_Tenis("federe","nadal","03-12-2025","Rolan Garros",[5,6,5,6],[1,1,1,5]) # ganado con 3 sets
            tenis3 = Partido_Tenis("federe","nadal","03-12-2025","Rolan Garros",[5,6,5,6],[4,7,4,5]) # resultado correcto

            tenis3.comprobar_partidos("federe","nadal","03-12-2025") # Comprobación de partidos

    @staticmethod
    def pausa():
        input("\nPulse Enter para continuar...")            
        os.system('clear' if os.name == 'posix' else 'cls')

if __name__ == "__main__":
    Main.main()