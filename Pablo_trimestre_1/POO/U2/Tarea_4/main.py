from embarcacion import Embarcacion
from lancha import Lancha
from velero import Velero

class Main:
    @staticmethod
    def main():
        try:
            v1 = Velero("Velero 1", 4, 2)
            print(v1)
            v2 = Velero("Velero 2", 4, 2)
            print(v2)
            v1.iniciar_navegacion(20, "ceñida", "Patrón 1", 3)
            v2.iniciar_navegacion(20, "ceñida", "Patrón 2", 3)
            print(v1)
            print(v2)
            print(v1.iniciar_regata(v2))
        except Exception as e:
            print(e)

if __name__ == "__main__":
    Main.main()
