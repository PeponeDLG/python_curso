import os
import csv
import json
from gestion_videojuegos import Gestion_Videojuegos

class Main:
    @staticmethod
    def main():
            os.system('clear' if os.name == 'posix' else 'cls')
            try:
                path = os.path.join(os.path.dirname(__file__),"VideoGame_Stats.csv")

                gv = Gestion_Videojuegos(path)

                print("---- Probamos la clase Gestion_Videojuegos con la lectura del archivo ----")
                gv.print_lista()

                input("\nPulse Enter para continuar...")            
                os.system('clear' if os.name == 'posix' else 'cls')

                print("\n\n ---- Leemos fichero FOR ----")
                gv.txt_by_cod_equipo("FOR")
                gv.read_txt("FOR")

                input("\nPulse Enter para continuar...")            
                os.system('clear' if os.name == 'posix' else 'cls')

                gv.muestra_total("Avanzado")

                gv.get_team_max()

                # gv.json_by_cod_equipo("medias")

            except Exception as e:
                print(e)

            

if __name__ == "__main__":
    Main.main()