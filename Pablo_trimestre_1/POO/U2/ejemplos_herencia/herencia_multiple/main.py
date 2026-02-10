from clases import Telefono, Dispositivo, Smartphone

class Main:
    @staticmethod
    def main():
        t1 = Telefono()
        print(t1.llamar(654321987))
        print(t1.colgar())
        print("-"*100)

        d1 = Dispositivo("Linux", 20)
        print(d1.info())
        print("-"*100)
        
        s1 = Smartphone("Motorola", "Android", 2)
        print(s1)
        print(s1.llamar(654321987))
        print(s1.colgar())
        print(s1.info())

if __name__ == "__main__":
    Main.main()
