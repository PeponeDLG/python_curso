'''1. Crea un array a partir de una lista de números con decimales (los que tu consideres, 4 o

5 números). Imprime sus valores uno a uno mediante un bucle while y los atributos del array

(dimensiones, tamaño, tipo de dato, shape).'''

import numpy as np

# Creamos una lista de números decimales
lista_decimales = [1.5, 2.3, 3.7, 4.1, 5.9]

# Convertimos la lista en un array de NumPy
array_decimales = np.array(lista_decimales)

# Inicializamos el índice para el bucle while
i = 0

# Imprimimos cada valor del array uno a uno
while i < array_decimales.size:
    print(f"Elemento {i}: {array_decimales[i]}")
    i += 1

# Imprimimos los atributos del array
print("Dimensiones:", array_decimales.ndim)
print("Tamaño:", array_decimales.size)
print("Tipo de dato:", array_decimales.dtype)
print("Shape:", array_decimales.shape)