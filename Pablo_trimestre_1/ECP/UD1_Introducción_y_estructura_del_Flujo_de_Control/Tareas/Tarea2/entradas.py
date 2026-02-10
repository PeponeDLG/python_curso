edad = int(input("Introduce la edad: "))

if edad < 4:
    print("Entrada gratuita")
elif edad <= 18:
    print("Entrada con descuento")
else:
    print("Entrada normal")
