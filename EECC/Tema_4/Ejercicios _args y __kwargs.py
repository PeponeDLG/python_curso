import os
os.system("cls") if os.name.lower() =="win32" else os.system("clear")

def inter(num):
    input("\npresione enter para continuar...")    
    os.system("cls") if os.name.lower() =="win32" else os.system("clear")
    print(f"Ejercicio {num}")
    input("\npresione enter para continuar...\n")    

# Ejercicio 1 - Validador flexible de mínimos-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(1)
def minimo(*nums):
    if len(nums) == 0:
        raise ValueError("Error: Introduzca al menos un número como argumento.")

    minimo = nums[0]        # Toma como referencia el primer arg
    for num in nums:
        if num < minimo:
            minimo = num    # Si algún otro argumento es menor, se sobreescribe

    return minimo

# Pruebas (descomentar):
print(minimo(3, 2, 5, 3, 4, 1, 3, 6))
# print(minimo())


# Ejercicio 2 - Suma con “modo” -- -- -- -- --- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(2)
def suma_modo(*nums, modo="normal"):
    opcion = modo
    suma = 0
    match opcion:
        case "normal":
            for num in nums:
                suma += num
        case "abs":
            for num in nums:
                suma += abs(num)
        case "solo_pares":
            for num in nums:
                if not num % 2:
                    suma += num
        case _:
            raise ValueError("Error: modo no válido.")

    return suma

# Pruebas (descomentar):
print(suma_modo(2, 2))
# print(suma_modo(2, -2, modo="abs"))
# print(suma_modo(2, 3, 4, modo="solo_pares"))
# print(suma_modo(2, 2, modo="otro"))


# Ejercicio 3 - Logger configurable -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(3)

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

# Ejercicio 6 - Función “apply” tipo mini-framework-- -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(6)

def apply(func, *args, **kwargs):
    
    for i in kwargs:        
        print(f"{args[0]} al {kwargs[i]} = {func(args[0],kwargs[i])}")

def descuento(precio, porcentaje):
    return precio * (porcentaje/100)

apply(descuento,100,noventa=90,cincuenta=50,veinticinco=25)

# Ejercicio 4 - Construir URL con parámetros  -- ---- -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(4)
def build_url(base, **params):
    ordenados = sorted(params)
    url = base
    if len(ordenados) > 0:
        url += "?"

    for i in ordenados:
        url += f"&{i}={params[i]}"

    return url

# Pruebas (descomentar):  
print(build_url("https://site.com", q="python", page=2))  # Nota: En el ejemplo no ordena los params. Aquí sí
# print(build_url("https://site.com"))

# Ejercicio 5 - Mezcla de listas con *args -- -- ---- -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(5)
# Función secundaria para intercalar las cadenas
def intercalar(cadenas):
    for i in cadenas:
        lista_impares = list()  # Lista con los elementos de índice impar
        lista_pares = list()    # Lista con los elementos de índice par
        for i in range(len(cadenas)):
            if i % 2:
                lista_pares.append(cadenas[i])
            else:
                lista_impares.append(cadenas[i])

        salida = zip(lista_pares, lista_impares)    

        return [elem for elem in salida]

def mezclar_listas(*listas, modo="intercalar"):
    opcion = modo
    cadena = str()
    match modo:
        case "intercalar":
            resultado = intercalar(listas)
            for i in resultado:
                for j in i:
                    cadena += j
        case "concatenar":
            for i in listas:
                cadena += i
           
    return cadena

# Pruebas (descomentar):
print(mezclar_listas("uno", "dos", "tres", "cuatro"))
# print(mezclar_listas("uno", "dos", "tres", "cuatro", modo="concatenar"))

# Ejercicio 6 - Función “apply” tipo mini-framework-- -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(6)
    
    

# Ejercicio 7 - Normalizador de notas (firma “pro”)-- -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(7)

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

# Ejercicio 8 - Diccionario “merge” con reglas- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(8)

def merge_dicts(*dicts, **kwargs):
    
    modo = kwargs.get("modo", "suma")
    
    dicc = dict()
        
    for d in dicts:
        for i in d:
            if i in dicc:
                if type(dicc[i]).__name__.lower() == "int":
                    if modo == "suma":
                        dicc[i] += d[i]
                    else:
                        dicc[i] = d[i]
                        
                if type(dicc[i]).__name__.lower() == "str":
                    if modo == "lista":
                        if not isinstance(dicc[i], list):
                            dicc[i] = [dicc[i]]
                        dicc[i].append(d[i])
                    else:
                        dicc[i] = d[i]
            else:
                dicc[i] = d[i]

    return dicc

print(merge_dicts({"nombre":"pepe", "edad":42},{"nombre":"antonio", "edad":42},modo="lista"))  
    


# Ejercicio 9 - Función de facturación flexible -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(9)

def factura(cliente_id, *importes, **kwargs):
    
    res ={
        "cupon" : kwargs.get("cupon",0),
        "iva" : kwargs.get("iva",0.21),
        "envio" : kwargs.get("envio",0),
        "desglose" : kwargs.get("desglose",False)
        }

    print(f"Total factura para '{cliente_id}': {((sum(importes) - sum(importes)*res["cupon"]) * (1+res["iva"]) + res["envio"])}")
    
    if res["desglose"]:
        return res

print(factura("Moreno",5,1,6,desglose=True))

# Ejercicio 10 - Validación de parámetros “estricta” - -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(10)

def configurar_app(**kwargs):
    modo = kwargs.get("modo","auto")
    debug = kwargs.get("debug",False)
    timeout = kwargs.get("timeout",10)
    
    res = {"modo":modo,"debug":debug,"timeout":timeout}
    
    try:
        if type(debug).__name__.lower() != "bool":
            raise Exception("El parámetro 'debug' debe ser booleano")
        if timeout < 0:
            raise Exception("El parámetro 'timeout' debe ser positivo")
        
        for i in kwargs:
            if i != "modo" and i != "debug" and i != "titimeoutm":
                raise Exception(f"El parámetro '{i}' es incorrecto.")
    except Exception as e:
        print(f"¡¡Error!!! -> {e}\n")       
    
    
    return res

print(configurar_app(debug="lala"))


# Ejercicio 11 - Desempaquetado obligatorio -- -- -- - -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(11)

def saludo(nom, anios, ciud, *args, **kwargs):
    print(f"Saludo posicionales: {nom}, {anios}, {ciud}")
    print(f"Saludo args: {args[0]}, {args[1]}, {args[2]}")
    print(f"Saludo posicionales: {kwargs["nombre"]}, {kwargs["edad"]}, {kwargs["ciudad"]}")
    
saludo("pepe",42,"Córdoba","Antonio",30,"Málaga",nombre="Fulano",edad=28,ciudad="Bilbao")

# Ejercicio 12 - Mini-reto: firma limpia y extensible- -- -- -- -- -- -- -- -- -- -- -- -- -- 
inter(12)

def numeros(l:list):
    print(f"Suma  -> {sum(l)}")
    print(f"Media -> {sum(l)/len(l)}")
    print(f"Min   -> {min(l)}")
    print(f"Max   -> {max(l)}")
    
def letras(l:list):
    print(f"Cantidad -> {len(l)}")
    print(f"Larga -> {max(l)}")
    print(f"Corta -> {min(l)}")

def procesar(*args, **kwars):
    
    lNum = list()
    lStr = list()
    modo = kwars.get("modo","auto")
    verb = kwars.get("verbose",False)
    
    for i in args:
        if type(i).__name__.lower() == "int":
            lNum.append(i)
        elif type(i).__name__.lower() == "str":
            lStr.append(i)
                
    if verb == True:
        print("Contenido de args:")
        for i in args:
            print("-> ",i)
        print("\nContenido de kwargs:")
        for i in kwars:
            print("-> ",kwars[i])
        
    
    numeros(lNum) if len(lNum) > 0 else None
    letras(lStr) if len(lStr) > 0 else None    
        
procesar("aa",2,"aaaaa",2,verbose=True)
    
