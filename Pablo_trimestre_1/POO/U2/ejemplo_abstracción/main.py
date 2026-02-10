from clases import *

class Main:
    @staticmethod
    def main():
        # Si intentamos crear una instancia de una clase abstracta obtenemos un TypeError
        # e1 = Empleado("Miguel", 1500)

        d1 = Director("Miguel", 1500, 500)
        print(d1.get_info())

        v1 = Vendedor("María", 1200, 400)
        print(v1.get_info())

if __name__ == "__main__":
    Main.main()
