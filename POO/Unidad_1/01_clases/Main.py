# Importamos la clase Coche desde el archivo coche.py
from coche import Coche

# Creamos distintos objetos de la clase Coche con valores personalizados
coche1 = Coche("Amarillo", "Ferrari", "Aventador", 300, 500, 2)
coche2 = Coche("Verde", "Porsche", "911", 250, 400, 2)
coche3 = Coche("Negro", "Lamborghini", "Aventador", 300, 500, 2)
coche4 = Coche("Rosa", "Seat", "Ibiza", 250, 200, 5)

# Mostramos la información de cada coche usando el método getInfo()
print(coche1.getInfo())
print(coche2.getInfo())
print(coche3.getInfo())
print(coche4.getInfo())

# Atributo de clase
print(f"Se han creado {Coche.contador} coches en total")  # Acceso a un atributo de clase desde la clase
print(f"Se han creado {coche1.contador} coches en total") # Acceso a un atributo de clase desde una instancia