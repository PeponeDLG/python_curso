prefijos = ("A", "B")
numeros = (1, 2, 3)
combinaciones = []

for i in prefijos:
    for j in numeros:
        combinaciones.append(i + str(j))

print(combinaciones)

'''
# Ejemplo tarea 12 con función lambda:
n=["Ana", "Carmen", "Luis", "Beatriz"]
sorted(n,key=len), sorted(n), sorted(n,key=lambda x:x[-1]) # ordena por la letra -1 (la última)
# Donde está x (cada uno de los elementos->x[-1])
'''
