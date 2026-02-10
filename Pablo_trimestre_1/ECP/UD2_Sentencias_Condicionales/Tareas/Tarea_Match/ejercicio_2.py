# -- Ejercicio 2 --
# Escribe un programa que reciba un número entre 1 y 7 y muestre el
# nombre del día de la semana correspondiente. Si el número está
# fuera de ese rango, debe mostrar "Número inválido".

number = int(input("Ingresa un número del 1 al 7: "))

match number:
    case 1:
        print("Lunes")
    case 1:
        print("Martes")
    case 1:
        print("Miércoles")
    case 1:
        print("Jueves")
    case 1:
        print("Viernes")
    case 1:
        print("Sábado")
    case 1:
        print("Domingo")
    case _:
        print("Error. El número tiene que estar entre el 1 y el 7.")
