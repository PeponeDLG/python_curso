'''2. Crear una función “inicializar_array” que reciba por parámetro un array de 1 
dimensión de tipos enteros y devuelva el array inicializado/modificado con valores introducidos por teclado (solamente enteros). Utilizar un while para recorrer el array.
def inicializar_array(arr):'''

import numpy as np

# Preguntamos al usuario cuántos elementos tendrá el array
tam = int(input("¿Cuántos elementos tendrá el array? "))

# Creamos el array con ceros y tipo entero
mi_array = np.zeros(tam, dtype=int)

# Definimos la función que inicializa el array con valores introducidos por teclado
def inicializar_array(arr):
    i = 0
    while i < arr.size:
        valor = int(input(f"Introduce valor entero para la posición {i}: "))
        arr[i] = valor
        i += 1
    return arr

# Llamamos a la función para rellenar el array
mi_array = inicializar_array(mi_array)

# Mostramos el array final
print("Array inicializado:", mi_array)
