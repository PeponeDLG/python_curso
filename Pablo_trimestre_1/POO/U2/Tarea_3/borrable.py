class MiLista:
    def __init__(self, items):
        self.items = items

    def __iadd__(self, other):
        self.items.extend(other.items) # Agrega los elementos del otro objeto
        return self # Devuelve el objeto modificado

    def __repr__(self):
        return f"MiLista({self.items})"

# Creación de objetos
lista1 = MiLista([1, 2, 3])
lista2 = MiLista([4, 5, 6])

# Sobrecarga de +=
lista1 += lista2

# Resultado
print(lista1)
# Salida: MiLista([1, 2, 3, 4, 5, 6])
