cuadrados = []

for num  in range(1,6):
    cuadrados.append(num**2)

print(cuadrados)

# Compresión
cuadrados[num**2 in range(1,6)]
print(cuadrados)

del cuadrados
cuadrados = [num**2 for num in range(1,6)]
print(cuadrados)

cuadrados_pares = [num**2 for num in range(1,6) if num % 2 == 0]
print(cuadrados_pares)


letras = ['a','b']
numeros = [1,2]

combinaciones = [letra + str(numero) for letra in letras for numero in numeros]
print(combinaciones)

clasificacion = ["par" if num % 2 == 0 else "impar" for num in range(1,6)]
print(clasificacion)

cuadrados_dict = {num: num**2 for num in range(1,6)}
print(cuadrados_dict)


cuadrados_dict = {"numero " + str(num): num**2 for num in range(1,6)}
print(cuadrados_dict)
