print("\n=============================================================================\n")

def suma(l:list, posicion:int) -> int:
    if posicion >= 0:
        return int(l[posicion]) + suma(l, posicion-1)
        
    return 0

lista = [6,4]

print(suma(lista,lista.__len__()-1))



exit()
print("\n=============================================================================\n")

def factorial(n:int):
    if n > 1:
        res = n * factorial((n-1))
        return res
    elif n == 0 or n == 1:
        return 1
    else:
        raise ValueError("n debe ser mayor de 0")
    
print(factorial(10))