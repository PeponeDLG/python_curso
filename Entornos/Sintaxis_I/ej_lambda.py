numeros=[5,2,8,1,9]

ordenada = sorted(numeros, key=lambda x:x)
print(ordenada)
ordenada = sorted(numeros, key=lambda x:-x)
print(ordenada)

palabras = ["manzana","pera","kiwi","nadanja"]
ordenada = sorted(palabras, key=lambda x:len(x))

print(ordenada)

puntos = [10,25,5,30]
maximo = max(puntos,key=lambda x: x%20) # devolverá el que tenga mayor número dividido por 20
print(maximo)

personas = [("Ana",28),("Bob",22),("Carlos",35)]
ordenada_por_edad = sorted(personas,key=lambda x:x[1])
print(ordenada_por_edad)

precios = {"manzana":1.5,"banana":0.8,"naranja":1.2}

ordenados_por_precio = sorted(precios, key=lambda x:x[1]) # aquí coge de precios solo las claves
print(ordenados_por_precio)

print(max(precios.items(),key=lambda item:item[1])) # aquí coge de precios los items completos

numeros_set = {3,1,4,1,5,9}
lista_numeros = list(numeros_set)
print(numeros_set)
print(lista_numeros)

