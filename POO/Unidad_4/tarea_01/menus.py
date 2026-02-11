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
          
          7. Salir
          ---------------------------
          opción: 
          """)
    
    if str(opc).isnumeric() != True or int(opc) < 1 or int(opc) > 7:
        opc = 0
    
    return opc

def agregar_libro():
    lista =[]
    ok = False
    
    while ok == False:
        lista.append(input("Introduzca título: "))
        lista.append(input("Introduzca autor: "))
        lista.append(input("Introduzca isb: "))
        
        if len(lista[0]) == 0 or len(lista[1]) == 0 or len(lista[2]) == 0:
            lista = []
            input("Faltan campos por rellenar...")
        else:
            return Libro(lista[2],lista[0],lista[1],1)

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')
    