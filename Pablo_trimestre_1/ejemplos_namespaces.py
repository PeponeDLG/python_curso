# Ejemplo que explica el ámbito de las variables en Python y cómo las gestiona:
# https://j2logo.com/python/tutorial/espacios-de-nombres-modulos-y-paquetes/

# Cada objeto de un script tiene un entero asociado que es único e invariable durante su vida.
# También tiene uno, ninguno o varios identificadores que son el nombre o nombres del objeto.
# Por ejemplo:
# x = 1
# y = 1
# id(x) va a ser igual que id(y) puesto que '1' es un objeto en Python y en este caso tiene 2
# identificadores, que son 'x' e 'y'.

# Tipos de identificadores:
# - Protegidos (_*): No se importan de los módulos.
# - Del sistema (__*__)
# - Privados de clase (__*)

# Ambitos de una variable:
def funcion_a():
    y = 2
    def funcion_b():
        z = 3
        print(z)
        print(locals())     # La única variable local de este ámbito es z

    funcion_b()
    print(y)
    print(locals())         # Las variables locales aquí son funcion_b y 'y'

x = 1
funcion_a()
print(x)
print(locals())             # Como estamos en la zona más exterior del script, locals coincide con globals.

print(globals())            # Diccionario con los espacios de nombres. Clave: identificador del objeto. Valor: su valor.
print(id(__name__))         # Entero asociado del objeto __name__.
print(id(__doc__))          # Entero asociado del objeto __name__.

# Por ejemplo __name__ es un objeto global que como se escribe así: __*__ es un identificador del sistema.
# Su id es 10781944, su identificador es __name__ y su valor es __main__.

# Si definimos una variable como global con la palabra reservada 'global', su presencia excede a su ámbito
