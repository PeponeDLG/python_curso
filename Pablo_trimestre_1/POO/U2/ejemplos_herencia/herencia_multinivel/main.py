from clases import *

class Main:
    @staticmethod
    def main():
        p1 = Persona("Carlos", "García", 1.80, 40)
        print(p1)
        print(p1.hablar())
        print(p1.caminar())
        print(p1.dormir())
        print("-"*100)

        i1 = Informatico("Paco", "Perez", 1.78, 27)
        
        try:
            i1.insertarLenguajes("Java", 2)
            i1.insertarLenguajes("Bash", 5)
        except ValueError as e:
            print(e)

        print(i1)
        print(i1.hablar())
        print(i1.caminar())
        print(i1.dormir())
        print(i1.programar())
        print("-"*100)

        t1 = TecnicoRedes("Perico", "Gonzalez", 1.85, 58, "Pentesting")

        try:
            t1.insertarLenguajes("Ruby", 2)
            t1.insertarLenguajes("JavaScript", 5)
        except ValueError as e:
            print(e)

        print(t1)
        print(t1.hablar())
        print(t1.caminar())
        print(t1.dormir())
        print(t1.programar())        

if __name__ == "__main__":
    Main.main()
