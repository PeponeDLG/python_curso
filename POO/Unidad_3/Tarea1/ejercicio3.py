import os

class Ejercicio3:
    @staticmethod
    def ejercicio():
        try:
            ruta = os.path.join(os.path.dirname(__file__), "operaciones.txt")
            ruta_add = os.path.join(os.path.dirname(__file__), "mas_operaciones.txt")
            texto_add = str
            
            with open(ruta_add,"r",encoding="UTF-8") as add:
                texto_add = str(add.read())

            with open(ruta,"a",encoding="UTF-8") as txt:
                for linea in texto_add:
                    txt.write(linea)

            with open(ruta,"r",encoding="UTF-8") as txt:
                print("\n -- texto modificado -- \n")
                print(txt.read())
                
        except IOError as io:
            print("Error IO: ",io)
        else:
            print("\n -- fin de fichero -- \n")

        