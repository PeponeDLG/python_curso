temp = float(input("Introduce una temperatura: "))

if 10 <= temp < 26:
    print("Templado")
elif 26 <= temp < 35:
    print("Caluroso")
elif temp >= 35:
    print("Muy caluroso")
else:
    print("Fuera de rango")
