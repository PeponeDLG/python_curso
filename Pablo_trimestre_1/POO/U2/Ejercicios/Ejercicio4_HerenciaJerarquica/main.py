from clases import *

class Main:
    @staticmethod
    def main():
        v1 = Vehiculo("Toyota", "Auris", 2010)
        co1 = Coche("Opel", "Corsa", 2003, 3)
        m1 = Moto("Derby", "Variant", 1998, 49)
        ca1 = Camion("Pegaso", "Comet", 1972, 40)

        print(v1)
        print(v1.arrancar())
        print(v1.detener())
        print("-"*100)

        print(co1)
        print(co1.arrancar())
        print(co1.detener())
        print("-"*100)

        print(m1)
        print(m1.arrancar())
        print(m1.detener())
        print("-"*100)

        print(ca1)
        print(ca1.arrancar())
        print(ca1.detener())
        print("-"*100)

if __name__ == "__main__":
    Main.main()
