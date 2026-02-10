'''3.  Crear  las  funciones  “media”,  “máximo”,  “mínimo”  que  reciba  un  array  de  valores numéricos   y   devuelva
   la   media   aritmética,   el   valor   máximo   y   el   valor   mínimo respectivamente. Realizar el cálculo manualmente 
   recorriendo el array con un while.'''
import numpy as np

# Función para calcular la media aritmética
def media(arr):
    suma = 0
    i = 0
    while i < arr.size:
        suma += arr[i]
        i += 1
    return suma / arr.size

# Función para calcular el valor máximo
def máximo(arr):
    max_val = arr[0]
    i = 1
    while i < arr.size:
        if arr[i] > max_val:
            max_val = arr[i]
        i += 1
    return max_val

# Función para calcular el valor mínimo
def mínimo(arr):
    min_val = arr[0]
    i = 1
    while i < arr.size:
        if arr[i] < min_val:
            min_val = arr[i]
        i += 1
    return min_val

# Ejemplo de uso
datos = np.array([4, 7, 2, 9, 5])
print("Media:", media(datos))
print("Máximo:", máximo(datos))
print("Mínimo:", mínimo(datos))