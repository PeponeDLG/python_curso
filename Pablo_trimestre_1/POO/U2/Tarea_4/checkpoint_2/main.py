from embarcacion import Embarcacion
from lancha import Lancha
from velero import Velero

class Main:
    @staticmethod
    def main():
        v1 = Velero("Veleroide", 4, 2)
        v1.rumbo = "jkfdsl"
        print(v1)
        print(v1.rumbo)

        # l1 = Lancha("Lanchoide", 3, 2, 20)
        # print(l1)

if __name__ == "__main__":
    Main.main()
