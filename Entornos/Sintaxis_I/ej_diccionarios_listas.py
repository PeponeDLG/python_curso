# Diccionario

# Formas de declarar un diccionario
lenguajes = {'C':1972,'python':1991,'Java':1996} 
lenguajes = dict(Pascal=1970, C=1972, Python=1991, Java=1996)
lenguajesAntiguos = ['Assembler', 'Lisp','Pascal']
lenguajesAntiguos = dict.fromkeys(lenguajesAntiguos, 0) # Asigna el valor 0 a todas las claves

print(lenguajes['C'])
print(lenguajes.get('C'))

# print(lenguajes['C++']) # Error no controlado
print(lenguajes.get('C++')) # No da error, devuelve None
print(lenguajes.get('C++',"no se encuentra")) # Así podemos decir qué mensaje sale si no encuentra el elemento

lenguajes.pop('C')
print(lenguajes)

print('BASIC' in lenguajes)


for valor in lenguajes.values():
    print(valor)

for keys in lenguajes.keys():
    print(keys)

for clave, valor in lenguajes.items():
    print(clave,' - ', valor)

print(sorted(lenguajes)) # por defecto ordena por clave

print(sorted(lenguajes,key=lenguajes.get)) # ordena por valor -> en este caso .get es una propiedad no un método
print(type(lenguajes.get))

#Listas
frase = "hola mundo"
palabras = frase.split()
for palabra in palabras:
    print(palabra)

print(frase.find("undo"))
print(frase.find("ando"))