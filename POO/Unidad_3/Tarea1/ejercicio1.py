import os

class Ejercicio1:
    @staticmethod
    def ejercicio():
        try:
            ruta = os.path.join(os.path.dirname(__file__),"operaciones.txt")

            with open(ruta,"r",encoding="UTF-8") as txt:
                texto = txt.read()
                print(texto)
                
        except IOError as io:
            print("Error IO: ",io)
        else:
            print("\n -- fin de fichero -- \n")

        