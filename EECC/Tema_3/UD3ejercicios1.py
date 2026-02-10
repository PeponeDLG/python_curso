import os 

os.system('clear' if os.name == 'posix' else 'cls')

print("Ejercicio 1")
print("-----------\n")
colores = ("rojo", "verde", "azul")
[print(i.upper()) for i in colores]

input("Pulse enter para continuar...")
os.system('clear' if os.name == 'posix' else 'cls')

print("\nEjercicio 2")
print("-----------\n")
edades = [15, 22, 18, 30, 16]
[print(i) for i in edades if i >= 18]

input("Pulse enter para continuar...")
os.system('clear' if os.name == 'posix' else 'cls')

print("\nEjercicio 3")
print("-----------\n")
frutas = ["manzana", "banana", "pera", "uva"]
[print(i,"- ",f) for i,f in enumerate(frutas)]

input("Pulse enter para continuar...")
os.system('clear' if os.name == 'posix' else 'cls')

print("\nEjercicio 4")
print("-----------\n")
notas = [6, 8, 9, 4, 7]
[print("Alumno ",i+1,": nota",f) for i,f in enumerate(notas)]

input("Pulse enter para continuar...")
os.system('clear' if os.name == 'posix' else 'cls')

print("\nEjercicio 5")
print("-----------\n")
[print(i) for i in range(0,21,2)]

input("Pulse enter para continuar...")
os.system('clear' if os.name == 'posix' else 'cls')

print("\nEjercicio 6")
print("-----------\n")

a = str

while True:
    a = input("Introduzca un número: ")
    
    if a.isnumeric():
        break
    print("¡Debe ser un número!")
    
[print(a,"x",i," = ",i*int(a)) for i in range(0,11)]

input("Pulse enter para continuar...")
os.system('clear' if os.name == 'posix' else 'cls')

print("\nEjercicio 7")
print("-----------\n")
nombres = ["Ana", "Luis", "Carlos"]
edades = [20, 25, 30]

[print(n," tiene ",e," años.") for n,e in zip(nombres,edades)]

input("Pulse enter para continuar...")
os.system('clear' if os.name == 'posix' else 'cls')

print("\nEjercicio 8")
print("-----------\n")
productos = ["pan", "leche", "huevos"]
precios = [1.2, 0.9, 2.5]

[print(i," - ",j,"€") for i,j in zip(productos,precios)]

input("Pulse enter para continuar...")
os.system('clear' if os.name == 'posix' else 'cls')

print("\nEjercicio 9")
print("-----------\n")

[print(i**2) for i in range(1,11)]

input("Pulse enter para continuar...")
os.system('clear' if os.name == 'posix' else 'cls')

print("\nEjercicio 10")
print("-----------\n")

numeros = [1, 2, 3, 4, 5, 6]
[print(i) for i in numeros if i%2==0]

input("Pulse enter para continuar...")
os.system('clear' if os.name == 'posix' else 'cls')

print("\nEjercicio 11")
print("-----------\n")

palabras = ["sol", "mar", "montaña", "río"]
[print(i," -> ",i.__len__()) for i in palabras]

input("Pulse enter para continuar...")
os.system('clear' if os.name == 'posix' else 'cls')

print("\nEjercicio 12")
print("-----------\n")

numeros = [1, 2, 3, 4, 5]
[print(i*2) for i in numeros if i > 2]

