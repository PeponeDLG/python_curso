import os
os.system("clear")
# Ejercicio 7
def normalizar_notas(*notas, redondeo=2, **kwars):
    min = kwars.get("minimo",0)
    max = kwars.get("maximo",10)
    modo = kwars.get("modo","clamp")

    res = list()

    for i in notas:
        if i < min or i > max:
            if modo=="error":
                raise Exception(f"Nota {i} fuera del rango {min} - {max}")
        else:
            res.append(float(i).__round__(redondeo))

    return(res)

print(normalizar_notas(5,8,3.8999,2,1,0,10,2,6,9,redondeo=3,minimo=2, maximo=5))

exit()

# Ejercicion 6
def apply(func, *args, **kwargs):
    
    for i in kwargs:        
        print(f"{args[0]} al {kwargs[i]} = {func(args[0],kwargs[i])}")

def descuento(precio, porcentaje):
    return precio * (porcentaje/100)

apply(descuento,100,noventa=90,cincuenta=50,veinticinco=25)

# Ejercicio 3
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

def opcionales(pepe="", pablo="-"):
    pass

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


