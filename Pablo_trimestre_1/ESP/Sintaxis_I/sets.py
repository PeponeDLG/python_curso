# Son como diccionarios pero sin valores, sólo claves
s = { 1, 2, 4 }
print(s)
s.add(5)
print(s)

# Operaciones con conjuntos
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # Devuelve lo mismo que print(a.union(b))
print(a - b)    # Devuelve los elementos de a restando los que también estén en b
print(a & b)    # Devuelve la intersección
print(a ^ b)    # XOR

# IMPORTANTE: sorted() no funciona con sets. Hay que convertirlos antes con list(nombre_del_set)
