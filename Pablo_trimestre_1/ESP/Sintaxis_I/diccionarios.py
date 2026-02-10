# lenguajes = { 'C': 1972, 'Python': 1992, 'Java': 1996 }
lenguajes = dict(Java = 1996, C = 1972, Python = 1991)  # Es otra forma de hacerlo

print(lenguajes['C'])                           # 1972
print(lenguajes.get('C++'))                     # Devuelve None (sin el get lanzaría una excepción)
print(lenguajes.get('C++', "No se encuentra"))  # Cambia el None por un mensaje
print(lenguajes)
print('BASIC' in lenguajes)                     # Devuelve False
# print(lenguajes.pop('C'))                       # Además de borrarlo lo devuelve
print(lenguajes)

for clave in lenguajes:
    print(lenguajes.get(clave))

print(sorted(lenguajes))        # Devuelve una lista con las claves ordenadas
print(lenguajes)
print(sorted(lenguajes, key=lenguajes.get))     # el .get aquí va sin () porque es una propiedad

for clave in lenguajes:             # Ordena por clave
    print(lenguajes.get(clave))

for clave in sorted(lenguajes, key=lenguajes.get):      # Ordena por valor
    print(lenguajes.get(clave))

# split() hace lo contrario que join()

diccionario_vacio = dict()      # Crea un diccionario vacío
# diccionario_vacio = {}        # Lo mismo
