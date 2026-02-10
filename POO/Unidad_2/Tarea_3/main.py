from cadena import Cadena

if __name__=="__main__":

    print("\n-> sumar datos de una cadena\n")
    cadena1 = Cadena("Me gusta programar en ")
    cadena2 = Cadena("Python")

    print(cadena1 + cadena2)

    print("\n\n-> nrestar objetos cadena\n")
    cadena1 = Cadena("El temor de un hombre sabio")
    cadena2 = Cadena("tormenta")

    print(cadena1 - cadena2)
    print(cadena1)

    print("\n\n-> Longitud de una instancia de cadena\n")

    cadena1 = Cadena("Leí 'La Rueda del Tiempo'")
    print(len(cadena1))

    print("\n\n-> Comparar objetos cadena\n")

    cadena1 = Cadena("Python")
    cadena2 = Cadena("Cobol")
    cadena3 = Cadena("Java")
    print(cadena1 == cadena2)
    print(cadena2 == cadena3)

    print("\n\n-> añadir valor str\n")

    cadena1 = Cadena("Sayonara ")
    cadena1 += "baby"
    print(cadena1)