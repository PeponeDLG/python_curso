# -- Ejercicio 1 --
# Escribe un programa que pida al usuario un número y determine si es positivo,
# negativo o cero.

number = input("Ingresa un número: ")

if int(number) > 0:
    print("El número es positivo")
elif int(number) < 0:
    print("El número es negativo")
else:
    print("El número es cero")

print(number)
