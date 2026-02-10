# Tuplas
# Podemos meterle elementos de distinto tipo.
# Se accede a cada elemento igual que en las listas.
dias = ('L', 'M', 'X', 'J', 'V', 'S', 'D')
elementos = ('a', 7, 'Hola qué tal')

#print(elementos[2])

# Podemos sumar tuplas
suma = dias + elementos
#print(suma)

# El primer elemento es el 0 pero el último es el -1
#print(dias[-1])

elementos_triplicado = 3 * elementos

# Ejemplos de slicing
#print(dias[1:4]) # Imprime los elementos 1, 2 y 3
#print(dias[:5]) # Imprime los elementos 0, 1, 2, 3 y 4

# Recorrer elementos con for
'''
for dia in dias:
    print(dia)
'''

# Recorrer elementos con while
'''
contador = 0
while contador < len(dias):
    print(dias[contador])
    contador += 1
'''

# Comprobar si un elemento está presente
#print('Hola qué tal' in elementos)

# Index y count
ganadores = ('Brasil', 'Italia', 'Brasil')
#print(ganadores.count('Brasil'))
#print(ganadores.index('Brasil', 1))
