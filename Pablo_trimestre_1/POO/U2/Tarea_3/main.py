from cadena import Cadena

class Main:
    @staticmethod
    def main():
        #try:
            # Crea instancias de Cadena
            c1 = Cadena("Me gusta programar en ")
            c2 = Cadena("Python")
            c3 = Cadena("El temor de un hombre sabio")
            c4 = Cadena("tormenta")
            c5 = Cadena("Leí 'La Rueda del Tiempo'")
            c6 = Cadena("Cobol")
            c7 = Cadena("Java")
            c8 = Cadena("Sayonara ")

            print("-- Prueba del método __add__: --")
            print(c1 + c2)
            print("-"*100)

            print("-- Prueba del método __sub__: --")
            print(c3 - c4)
            print("-"*100)

            print("-- Prueba del método __len__: --")
            print(len(c5))
            print("-"*100)

            print("-- Prueba del método __eq__: --")
            print(c2 == c6)
            print(c6 == c7)
            print("-"*100)

            print("-- Prueba del método __iadd__: --")
            c8 += "baby"
            print(c8)
            print("-"*100)


        #except Exception as e:
            #print(e)

if __name__ == "__main__":
    Main.main()
