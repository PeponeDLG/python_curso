# Importar la clase
from persona import Persona

# __init__() se ejecuta al crear los objetos
p1 = Persona("Ana", 25)
p2 = Persona("Luis", 30)
p3 = Persona("Ana", 25)

# __str__(): representación legible para el usuario
print("Usando __str__():", str(p1))   # "Ana, 25 años"

# __repr__(): representación para el programador
print("Usando __repr__():", repr(p1)) # "Persona(nombre='Ana', edad=25)"

# __eq__(): comparación de objetos
print("¿p1 == p2?", p1 == p2)   # False
print("¿p1 == p3?", p1 == p3)   # True

print("Pepe -> ",str(p1))

# __del__(): se llama cuando el objeto deja de existir
del p2   # fuerza la eliminación de p2