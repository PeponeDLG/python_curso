if __name__ == "__main__":
    try:
        ########################## Ejercicio 1 ##########################

        try:
            print("\n-- -- Ejercicio 1 -- -- \n")

            num = int(input("Introduzca un número real:"))

            if num < 0:
                print("El número es negativo")
            elif num > 0:
                print("El número es positivo")
            else:
                print("El número es cero")
        except:
            print("\n¡¡¡HE DICHO UN NÚMERO!!!")
            raises

        ########################## Ejercicio 2 ##########################

        try:
            print("\n\n-- -- Ejercicio 2 -- -- \n\n")
            ok = False

            while ok != True:
                dia = int(input("Introduzca un número del 1 al 7: "))
                ok = True

                match dia:
                    case 1:
                        print("\nHa elegido: Lunes")
                    case 2:
                        print("\nHa elegido: Martes")
                    case 3:
                        print("\nHa elegido: Miércoles")
                    case 4:
                        print("\nHa elegido: Jueves")
                    case 5:
                        print("\nHa elegido: Viernes")
                    case 6:
                        print("\nHa elegido: Sábado")
                    case 7:
                        print("\nHa elegido: Domingo")
                    case _:
                        print("\n¡HE DICHO DEL 1 AL 7!\n")
                        ok = False

        except:
            print("\n¡¡¡HE DICHO UN NÚMERO DEL 1 AL 7!!!\n")

        ########################## Ejercicio 3 ##########################
        try:
            tarifa = int

            print("\n-- -- Ejercicio 3 -- -- \n\n")

            print("Seleccione tipo de cliente")
            print("--------------------------\n")
            print("1 - PYME")
            print("2 - Corporativo")
            print("3 - Gobierno")
            print("4 - Cualquier otro\n")

            ok = False

            while ok != True:
                cliente = int(input("Seleccione un cliente: "))
                ok = True

                match cliente:
                    case 1:
                        tarifa = 50
                    case 2:
                        tarifa = 80
                    case 3:
                        tarifa = 65
                    case 4:
                        tarifa = 40
                    case _:
                        print("El número debe ser del 1 al 4: ")
                        ok = False

            print("\n")

            ok = False

            while ok != True:

                mes = int(input("Seleccione del 1 al 12 el mes que quiera calcular: "))
                ok = True

                if mes >= 1 and mes <= 7:
                    total = tarifa + (tarifa * 0.15)
                elif mes >= 8 and mes <= 12:
                    total = tarifa + (tarifa * 0.10)
                else:
                    ok = False

                if ok == True:
                    print("La tarifa es ", total, "€/hora")

        except Exception as e:
            print("\n¡¡¡Tienes que introducir solo números enteros!!!\n")
    except:
        pass
