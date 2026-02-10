while True:
    num_1 = float(input("Introduce el primer número: "))
    num_2 = float(input("Introduce el segundo número: "))
    option = int(input("""
    Introduce:
                    1 - Sumar
                    2 - Restar
                    3 - Multiplicar
                    4 - Dividir
                    5 - Salir
    """))

    if option == 1:
        print("El resultado de la suma es: ", num_1 + num_2)
    elif option == 2:
        print("El resultado de la resta es: ", num_1 - num_2)
    elif option == 3:
        print("El resultado de la multiplicación es: ", num_1 * num_2)
    elif option == 4:
        if num_2 == 0:  # Evita la división entre 0
            print("Error. No es posible dividir entre 0")
        print("El resultado de la división es: ", num_1 / num_2)
    elif option == 5:
        print("Saliendo...")
        break
    else:
        print("Error: Opción incorrecta.")
    