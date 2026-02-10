'''4. Crear la función “encontrar” (usando while) que reciba dos parámetros: un array numérico y un valor. La función debe buscar en el array si el “valor” se encuentra en él. La función debe devolver:
○   Si valor se encuentra en el array, devolver el índice (primera aparición)

○   Si el valor no se encuentra en el array, devolver -1.'''
import numpy as np

# Función que busca un valor en el array y devuelve su índice o -1 si no está
def encontrar(arr, valor):
    i = 0
    while i < arr.size:
        if arr[i] == valor:
            return i  # Devuelve el índice de la primera aparición
        i += 1
    return -1  # Si no se encuentra

# Ejemplo de uso
datos = np.array([10, 20, 30, 40, 50])
print("Array:", datos)
print("Índice del valor 30:", encontrar(datos, 30))
print("Índice del valor 99:", encontrar(datos, 99))
