numeros = [5, 2, 8, 1, 9]
ordenada = sorted(numeros, key=lambda x: x)
print(ordenada)

palabras = ["manzana", "pera", "kiwi", "naranja"]
ordenadas_por_longitud = sorted(palabras, key=lambda s: len(s))
print(ordenadas_por_longitud)

frutas = ["banana", "Uva", "fresa", "Mango"]
frutas.sort(key=lambda f: f.lower())    # Ordena ignorando mayúsculas
print(frutas)

personas = [("Ana", 28), ("Bob", 22), ("Carlos", 35)]

ordenadas_por_edad = sorted(personas, key=lambda x: x[1])
print(ordenadas_por_edad)

# A lambda se le pueden aplicar varios criterios así: (criterio1, criterio2)
