from pasword import *

if __name__=="__main__":
    valido=False
    longitud = 0

    while valido==False:
        long = input("Introduzca la longitud deseada para su clave: ")
        
        if str.isnumeric(long):
            if int(long) >= genera_password.longitud:
                longitud=int(long)
                valido = True
            else:
                print("\nLA LONGITUD MÍNIMA SON 8 CARACTERES\n")
        else:
            print("\nDEBE INTRODUCIR UN NÚMERO\n")


    pwd = genera_password(longitud)

    pwd.genera_password()

    print(pwd)

    if pwd.es_fuerte():
        print("\nLa contraseña es FUERTE")
    else:
        print("\La contraseña es débil")