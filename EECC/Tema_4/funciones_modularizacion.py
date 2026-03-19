import os
os.system("clear")
# **kwargs
def log(*args,**kwarg):
    sep = kwarg.get("sep"," ")
    end = kwarg.get("end","\n")
    prefix = kwarg.get("prefix","")
    upper = kwarg.get("upper",False)

    print(f"sep: {sep}")
    print(f"end: {end}")
    print(f"prefix: {prefix}")
    print(f"upper: {upper}")

    cadena = str()

    for i in args:        
        cadena += cadena + i + sep + end + prefix 

    if upper:
        cadena = str(cadena).upper()

    return cadena

print(log("mensaje 1","mensaje 2", "mensaje 3",sep="-",end="|",pepe="pepe"))

def opcionales(pepe="", pablo="-")

# *args -> args es por convención, pero podería ser *pepe -> el * es obligatorio

def ver_args(*args): # -> es una tupla
    print("args= ", args)
    print("tipo= ", type(args))
    print("len= ", len(args))
    print("Suma args=", sum(args))

def anunciar(titulo, *mensajes):
    print("TITULO: ",titulo)

    for m in mensajes:
        print("-",m)

ver_args(1,2,3)
ver_args()

anunciar("titulaso", "mensaje 1","mensaje 2")


def sumar(*args):
    return sum(*args)

nums = [1,2,3,4]
print("Sumar: ",sumar(nums))


exit()

# Parámetros nominales
def descuento(precio, porcentaje):
    return precio*(1-porcentaje)

print(descuento(porcentaje=0.1, precio=100)) # 

exit()

def precio_con_iva(precio, iva=0.21):
    return precio * (1+iva)


print(precio_con_iva(100))


