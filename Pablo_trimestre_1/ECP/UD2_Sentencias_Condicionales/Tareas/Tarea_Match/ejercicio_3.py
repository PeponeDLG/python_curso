# -- Ejercicio 2 --
# Una empresa de servicios de consultoría aplica diferentes tarifas (por hora)
# a sus clientes dependiendo de dos factores:
# -​ Tipo de Cliente: Esto determina la tarifa base.
# -​ Mes del Servicio: Esto determina si se aplica un recargo o un descuento
#   especial.

print("-- Calculadora de tarifas --")

client = input("Tipo de cliente: ")
match client:
    case "PYME":
        fee = 50
    case "Corporativo":
        fee = 80
    case "Gobierno":
        fee = 65
    case _:
        fee = 40

month = int(input("Mes: "))
if month < 8:
    plus = 1.15
else:
    plus = 0.9

print(f"Tarifa base por hora: {fee * plus}")
