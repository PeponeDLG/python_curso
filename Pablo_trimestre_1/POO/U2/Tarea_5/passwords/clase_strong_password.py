from passwords.clase_password import Password
import random

class Strong_password(Password):
    def __init__(self, passwd=None):
        super().__init__(passwd)

    # Método para generar contraseñas
    # Sobreescribe al método de la clase padre.
    # --- Funcionamiento: ---
    # - Elige aleatoriamente si el carácter será una mayúscula, minúscula, un número o un
    # símbolo.
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
                num_aleatorio = random.randint(1, 5)
                if num_aleatorio == 1:
                    passwd += chr(random.randint(97, 122)) # Letras minúsculas
                elif num_aleatorio == 2:
                    passwd += chr(random.randint(65, 90)) # Letras mayúsculas
                elif num_aleatorio == 3:
                    passwd += chr(random.randint(48, 57)) # Números
                elif num_aleatorio == 4:
                    passwd += chr(random.randint(33, 47)) # Símbolos
                else:
                    passwd += chr(random.randint(123, 125)) # Más símbolos
                    
        return passwd

    # Método para comprobar si una contraseña es fuerte
    # Sobreescribe al método de la clase padre.
    # --- Criterios: ---
    # - Debe tener al menos 15 caracteres.
    # - Debe tener al menos 2 minúsculas.
    # - Debe tener al menos 3 mayúsculas.
    # - Debe tener al menos 2 números.
    # - Debe tener al menos 2 caracteres especiales.
    # La función ord() convierte un carácter a su equivalente entero en la tabla ASCII.
    def es_fuerte(self):
        long = len(self.get_passwd)
        cant_minusculas = 0
        cant_mayusculas = 0
        cant_numeros = 0
        cant_simbolos = 0
        for i in self.get_passwd:
            if ord(i) in range(97, 123):
                cant_minusculas += 1
            elif ord(i) in range(65, 91):
                cant_mayusculas += 1
            elif ord(i) in range(48, 58):
                cant_numeros += 1
            elif ord(i) in range(33, 48) or ord(i) in range(23, 126):
                cant_simbolos += 1
        
        if long >= 15 and cant_minusculas >= 2 and cant_mayusculas >= 3 and cant_numeros >= 2 and cant_simbolos >= 2:
            return True
        else:
            return False
