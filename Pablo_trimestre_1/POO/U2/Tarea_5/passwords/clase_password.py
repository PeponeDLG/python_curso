import random

class Password:
    # Constructor que permite instanciar con y sin el parámetro
    def __init__(self, passwd=None):
        if passwd == None:
            self.__passwd = self.genera_passwd()
        else:
            if not isinstance(passwd,str):
                raise Exception("La contraseña debe ser una cadena")
            if len(self.__passwd) < 8:
                raise Exception("La contraseña debe tener más de 8 caracteres") 
            self.__passwd = passwd

    # Getter
    @property
    def get_passwd(self):
        return self.__passwd

    # Muestra en consola los datos del objeto
    def __str__(self):
        return f"Contraseña: {self.__passwd} | Longitud: {len(self.__passwd)} caracteres."

    # Genera una contraseña de la longitud deseada (mínimo 8 caracteres)
    # --- Funcionamiento: ---
    # - Elige aleatoriamente si el carácter será una mayúscula, minúscula o número.
    # - Concatena el carácter en la contraseña.
    # - Cuando se alcance el tamaño especificado, devuelve la contraseña como un string.
    def genera_passwd(self):
        passwd = ""
        try:
            long = int(input("Introduce la longitud (mínimo 8 caracteres): "))
        except ValueError:
            long = 8
            print("Error. No es un número de caracteres válido. Número de caracteres por defecto: 8")
        if long < 8:
            raise Exception("La contraseña debe tener al menos 8 caracteres")
        else:
            for i in range(long):
                num_aleatorio = random.randint(1, 3)
                if num_aleatorio == 1:
                    passwd += chr(random.randint(97, 122))
                elif num_aleatorio == 2:
                    passwd += chr(random.randint(65, 90))
                else:
                    passwd += chr(random.randint(48, 57))
                    
        return passwd
    
    # Comprueba si una contraseña es fuerte.
    # --- Criterios: ---
    # - Debe tener más de 10 caracteres.
    # - Debe tener más de una minúscula.
    # - Debe tener más de dos mayúsculas.
    # La función ord() convierte un carácter a su equivalente entero en la tabla ASCII.
    def es_fuerte(self):
        long = len(self.__passwd)
        num_minusculas = 0
        num_mayusculas = 0
        for i in self.__passwd:
            if ord(i) in range(97, 123):
                num_minusculas += 1
            elif ord(i) in range(65, 91):
                num_mayusculas += 1
        
        if long > 10 and num_minusculas > 1 and num_mayusculas > 2:
            return True
        else:
            return False
