import os

class Ejercicio2:
    @staticmethod
    def ejercicio():
        try:
            ruta = os.path.join(os.path.dirname(__file__), "operaciones.txt")

            with open(ruta,"r",encoding="UTF-8") as txt:
                cont = 0

                for linea in txt:
                    print(cont , ": " , linea.strip())
                    cont += 1
                
        except IOError as io:
            print("Error IO: ",io)
        else:
            print("\n -- fin de fichero -- \n")

        