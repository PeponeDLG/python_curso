import os
from libro import Libro

def menuPrincipal() -> bool:
    clear()
    
    opc = input("""
          ***************************
          Gestión de la biblioteca
          ***************************
          1. Mostrar libros
          2. Agregar libro
          3. Buscar libro
          4. Eliminar libro
          5. Prestar libro
          6. Devolver libro
          
          7. Salir
          ---------------------------
          opción: 
          """)
    
    if str(opc).isnumeric() != True or int(opc) < 1 or int(opc) > 7:
        opc = 0
    
    return opc

def agregar_libro() -> []:
    lista =[]
        
    lista.append(input("Introduzca título: "))
    lista.append(input("Introduzca autor: "))
    lista.append(input("Introduzca isb: "))
    
    if len(lista[0]) == 0 or len(lista[1]) == 0 or len(lista[2]) == 0:
        lista = []
        input("Faltan campos por rellenar...")
        return None
    
    return Libro(lista[2],lista[0],lista[1],1)

        
def libro_ibn():
    ok = False
    
    while ok == False:
        isbn = input("Introduzca ISBN: ")
        
        if str(isbn).isnumeric() != True or int(isbn) <= 0:
            lista = []
            input("ISBN incorrecto...")
        else:
            return isbn   
        
        
        
def titulo(titulo):
    clear()
    print(str(titulo).upper())
    print("="*str(titulo).__len__())

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')
    