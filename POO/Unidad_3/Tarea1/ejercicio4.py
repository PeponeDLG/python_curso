import os

class Ejercicio4:
    @staticmethod
    def ejercicio():
        try:
            ruta = os.path.join(os.path.dirname(__file__), "operaciones.txt")
            lista = []

            with open(ruta,"r",encoding="UTF-8") as txt:
                for linea in txt:
                    lista.append(linea)

            for linea in lista:
                if linea.__contains__("delete"):
                    print(linea)

            
                
        except IOError as io:
            print("Error IO: ",io)
        else:
            print("\n -- fin de fichero -- \n")

        