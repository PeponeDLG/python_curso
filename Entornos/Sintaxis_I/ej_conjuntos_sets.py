# Sets - No se pueden repetir los elementos, no se puede acceder individualmente y son inmutables ** No se pueden meter en sorted() **

s = {1,2,4}

listaNombres = 'Ana Pepe Juan Ana'.split()
print(listaNombres)

conjuntoNombres = set(listaNombres) # Al convertirlo en SET elimina los datos duplicados

print(conjuntoNombres)

s.add(5)
print(s)

a = {1,2,3,4}
b = {3,4,5,6}

print(a | b) # or -> coge lo que hay en a o en b
print(a & b) # and -> muestra lo que está en a y en b
print(a.union(b))
print(a - b) # quita de a los elementos que estén en b
print(a^b) # devuelve los elementos que no se repiten

