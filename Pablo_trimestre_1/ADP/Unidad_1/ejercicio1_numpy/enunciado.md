# Ejercicio 1 NumPy - Utilizar sólamente bucles while
1. Crea un array a partir de una lista de números con decimales (los que tu consideres, 4 o
5 números). Imprime sus valores uno a uno mediante un bucle while y los atributos del array
(dimensiones, tamaño, tipo de dato, shape).
2. Crear una función “inicializar_array” que reciba por parámetro un array de 1 dimensión de
tipos enteros y devuelva el array inicializado/modificado con valores introducidos por teclado
(solamente enteros). Utilizar un while para recorrer el array.
3. Crear las funciones “media”, “máximo”, “mínimo” que reciba un array de valores
numéricos y devuelva la media aritmética, el valor máximo y el valor mínimo
respectivamente. Realizar el cálculo manualmente recorriendo el array con un while.
4. Crear la función “encontrar” (usando while) que reciba dos parámetros: un array numérico
y un valor. La función debe buscar en el array si el “valor” se encuentra en él. La función
debe devolver:
- Si valor se encuentra en el array, devolver el índice (primera aparición)
- Si el valor no se encuentra en el array, devolver -1.
5. Crear una función “desviación estándar” que reciba por parámetro un array y devuelva la
desviación estándar. Calcular paso a paso el resultado utilizando un while para recorrer el
array. También se debe usar la función “media” del ejercicio 2. Para calcular la raíz
cuadrada podemos usar la función de numpy.sqrt(n). Operador potencia es **
