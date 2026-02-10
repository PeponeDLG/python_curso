import numpy as np

'''
# Muestra los valores recorriendo el array con un bucle while
while i < array.size:
    print(f"Elemento {i}: {array[i]}")
    i += 1

# Muestra los atributos del array
print(f"Dimensiones: {array.ndim}")
print(f"Tamaño: {array.size}")
print(f"Tipo de dato: {array.dtype}")
print(f"Shape: {array.shape}")

# Pide el tamaño del array
tam = int(input("¿Cuántos elementos tendrá el array? "))

# Recibe un array y lo modifica con el tamaño y valores indiintroducidos por el usuario
def inicializar_array(array):
    array = np.zeros(tam, int)
    i = 0
    while i < array.size:
        valor = int(input(f"Introduce un valor entero para la posición {i}: "))
        array[i] = valor
        i += 1
    
    return array

# Llama a la función para rellenar el array
array = inicializar_array(array)

# Muestra el array
print(f"Array inicializado: {array}")

'''
# Devuelve la media
def calcular_media(array):
    i = 0
    suma = 0
    while i < array.size:
        suma += array[i]
        i += 1

    return suma / array.size
'''

# Devuelve el valor máximo
def calcular_valor_maximo(array):
    i = 0
    max = 0
    while i < array.size:
        if array[i] > max:
            max = array[i]
        i += 1

    return max

# Devuelve el valor mínimo
def calcular_valor_minimo(array):
    i = 0
    min = array[0]
    while i < array.size:
        if array[i] < min:
            min = array[i]
        i += 1

    return min

# Busca un valor dado en un array. Si lo encuentra devuelve el índice, y si no, -1
def encontrar(array, valor):
    i = 0
    while i < array.size:
        if valor == array[i]:
            return i

        i += 1

    return -1

# Prueba la función
print(array)
print(encontrar(array, 6.5432))
'''

# Lista
list = [1, 2, 3, 4]

# Convierte la lista en array de NumPy
array = np.array(list)

'''
# Devuelve la desviación estándar
def calcular_desviacion_estandar(array):
    # Paso 1: Calcula la media
    i = 0
    sum = 0
    while i < array.size:
        sum += array[i]
        i += 1

    media = sum / array.size

    # Paso 2: Calcula la desviación de cada dato restándole la media
    desviaciones = np.zeros(array.size, int) # Inicializa el nuevo array con el tamaño del original
    i = 0
    while i < array.size:
        desviaciones[i] = array[i] - media
        i += 1

    # Paso 3: Eleva cada desviación al cuadrado y suma los resultados
    desviaciones_cuadrado = np.zeros(array.size, int) # Inicializa el nuevo array con el tamaño del original
    i = 0
    sum = 0
    while i < array.size:
        desviaciones_cuadrado[i] = desviaciones[i] ** 2
        sum += desviaciones_cuadrado[i]
        i += 1
    
    # Paso 4: Dividir el resultado anterior entre el número de datos obteniendo la varianza
    varianza = sum / array.size

    # Paso 5: Calcular la raíz cuadrada de la varianza obteniendo la desviación estándar
    return np.sqrt(varianza)
'''

# Devuelve la desviación estándar
def calcular_desviacion_estandar(array):
    # Calcula la suma del cuadrado de la desviación de cada dato respecto a la media
    i = 0
    sum = 0
    while i < array.size:
        sum += (array[i] - calcular_media(array)) ** 2
        i += 1

    # Divide el resultado entre el número de datos obteniendo la varianza y calcula su raíz cuadrada
    return np.sqrt(sum / array.size)

# Prueba la función
print(calcular_desviacion_estandar(array))
