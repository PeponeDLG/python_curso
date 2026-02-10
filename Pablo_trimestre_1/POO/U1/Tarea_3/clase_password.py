import random

class Password:

    # Constructor que permite instanciar con y sin el parámetro
    def __init__(self, passwd=None):
        if passwd == None:
            self.__passwd = self.genera_passwd()
        else:
            if not isinstance(passwd,str):
                raise Exception("La contraseña debe ser una cadena")

            self.__passwd = passwd
            if len(self.__passwd) < 8:
                raise Exception("La contraseña debe tener más de 8 caracteres")
            else:
                self.__long = len(passwd)

    '''
    # Getters (comentados porque no se usan en esta tarea pero sí más adelante)
    def get_passwd(self):
        return self.__passwd

    def get_long(self):
        return self.__long
    '''

    # Muestra en consola los datos del objeto
    def __str__(self):
        return f"Contraseña: {self.__passwd} con longitud {len(self.__passwd)}"

    # Genera una contraseña aleatoria de la longitud deseada (mínimo 8 caracteres)
    def genera_passwd(self):
        passwd = ""
        long = int(input("Introduce la longitud (mínimo 8 caracteres): "))
        if long < 8:
            print("Error: contraseña debe tener al menos 8 caracteres")
        else:
            # Rellena la contraseña hasta alcanzar el tamaño deseado
            # Genera un número aleatorio dentro de un rango, pero omite los caracteres no válidos
            # Decimales ASCII válidos: del 48 al 57, del 65 al 90 y del 97 al 122
            # Si el decimal generado es válido, lo convierte a carácter e inserta en la contraseña
            while len(passwd) < long:
                num = random.randint(48, 122) 
                if num in range(48, 58) or num in range(65, 91) or num in range(97, 123):
                    passwd += chr(num) 
        
        return passwd
