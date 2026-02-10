import os 

class Main:
    @staticmethod
    def main():
        ruta_absoluta = os.path.abspath(__file__)
        print("Ruta absoluta: ",ruta_absoluta)

        print("Nombre directorio:", os.path.dirname(__file__))

        # Manejo de ficheros de texto
        ruta = os.path.join(os.path.dirname(__file__)+"/prueba.txt")
        print("Ruta -> ",ruta)
        
        # Escritura
        with open(ruta,"w",encoding="utf-8") as texto:
            texto.write("Línea 1\n")
            texto.write("Línea 2\n")
            texto.write("Línea 3\n")

        with open(ruta,"w",encoding="utf-8") as texto:
            texto.write("Línea 4\n")
            texto.write("Línea 5\n")
            texto.write("Línea 6\n")

        # Añadir
        with open(ruta,"a",encoding="utf-8") as texto:
            texto.write("-- añadido --\n")

        # Lectura
        with open(ruta,"r",encoding="utf-8") as texto:
            txt = texto.read()
            print("\n-- Contenido del fichero --\n")
            print(txt) 

        with open(ruta,"r",encoding="utf-8") as texto:
            print("\n-- Contenido del fichero línea a línea --\n")
            print("Tipo: ", type(texto) ,"\n")
            for linea in texto.readlines():
                print(linea)

if __name__ == "__main__":
    os.system("clear")
    Main.main()