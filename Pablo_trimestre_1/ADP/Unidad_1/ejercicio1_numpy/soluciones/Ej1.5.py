'''5. Crear una función “desviación estándar” que reciba por parámetro un array y devuelva la desviación estándar. 
Calcular paso a paso el resultado utilizando un while para recorrer el array.  También  se  debe  usar  la  función  “media”  
del  ejercicio  2. Para calcular la raíz cuadrada podemos usar la función de numpy.sqrt(n). Operador potencia es **
def desviacion_estandar(arr)'''

import numpy as np

# Función para calcular la media aritmética
def media(arr):
    suma = 0
    i = 0
    while i < arr.size:
        suma += arr[i]
        i += 1
    return suma / arr.size

# Función para calcular la desviación estándar
def desviacion_estandar(arr):
    # Calculamos la media
    m = media(arr)

    # Sumamos los cuadrados de las diferencias
    suma_cuadrados = 0
    i = 0
    while i < arr.size:
        suma_cuadrados += (arr[i] - m) ** 2
        i += 1

    # Calculamos la varianza y la desviación estándar
    varianza = suma_cuadrados / arr.size
    desviacion = np.sqrt(varianza)
    return desviacion

# Ejemplo de uso
datos = np.array([2, 4, 4, 4, 5, 5, 7, 9])
print("Array:", datos)
print("Desviación estándar:", desviacion_estandar(datos))

