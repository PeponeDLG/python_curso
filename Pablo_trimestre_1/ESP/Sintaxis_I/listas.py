# Listas
# Son como tuplas pero dinámicas
mi_lista = [10, "hola", 25]
#print(mi_lista[1])
mi_lista[1] = "adios"
#print(mi_lista[1])

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

#print(numbers[::-2])
#print(numbers[-2::-2])
palabras = ["agua", "camino", "barco"]
palabras.sort()
print(palabras)
print(palabras.index('camino'))

palabras.insert(1, "nueva")
print(palabras)
