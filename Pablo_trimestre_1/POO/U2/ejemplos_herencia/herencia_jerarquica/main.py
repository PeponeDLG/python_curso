from clases import Persona, Cliente, Trabajador

class Main:
    @staticmethod
    def main():
        p1 = Persona("Francisco", "Lama", "paco@persona.es")
        print(p1)

        p2 = Cliente("Juan", "Gomez", "juan@cliente.es", 1, 3000)
        print(p2)

        p3 = Trabajador("Benito", "Muñoz", "benito@trabajador.es", 1, 2000)
        print(p1)

if __name__ == "__main__":
    Main.main()
