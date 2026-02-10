paises = ['Francia','Alemania','España']
capitales = ['París', 'Berlin', 'Madrid']

for pais, capital in zip(paises,capitales):
    print(f'{pais} capital {capitales}')

diccionario = dict(zip(paises, capitales))
print(diccionario)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10,20,30]
contador = 0

for key in keys:
    diccionario[key] = values[contador]
    contador += 1

print(diccionario)

dict2 = {'Thirty':31}
diccionario.update(dict2)
print(diccionario)


# Diccionarios anidados
sampleDict = {
    "class":{
        "studend":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}

print(sampleDict)

diccionarioA = {
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"New York"
}

clavesAQuitar=["name", "salary"]

restantes = {}

for key in diccionarioA:
    if key not in clavesAQuitar:
        restantes[key] = diccionarioA[key]

print(restantes)