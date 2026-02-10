class Cadena:
    def __init__(self, cadena:str):
        if not isinstance(cadena, str):
            raise TypeError("No es un string")

        self.__cadena = cadena

    @property
    def cadena(self):
        return self.__cadena

    @cadena.setter
    def cadena(self, cadena:str):
        self.__cadena = cadena

    # Sobrecarga de operadores:
    # Suma objetos Cadena
    def __add__(self, otra):
        return self.__cadena + otra.__cadena

    # Reemplaza por espacios las vocales de la primera cadena si dichas vocales aparecen en la segunda
    def __sub__(self, otra):
        vocales = 'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú' # Tupla con todas las vocales
        vocales_cadena_2 = [] # Registra las vocales de la segunda cadena
        for letra in otra.cadena:
            if letra in vocales: # Detecta las vocales de la segunda cadena para registrarlas
                vocales_cadena_2.append(letra)

        for letra in self.cadena:
            if letra in vocales_cadena_2: # Compara las vocales de la primera cadena con las encontradas en la segunda
                nueva_cadena = self.cadena.replace(letra, " ") # Y si la encuentra la reemplaza por un espacio

        return nueva_cadena

    # Concatena una cadena con quedando modificada la primera
    def __iadd__(self, string:str):
        # self.cadena.extend(string)

        return self.cadena + string

    # Sobrecarga de funciones incorporadas:
    # Devuelve el número de ocurrencias de vocales mayúsculas, minúsculas, con tilde y sin tilde
    def __len__(self):
        cont = 0
        vocales = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú'
        for letra in self.cadena:
            if letra in vocales:
                cont += 1

        return cont

    # Compara el número de vocales de dos cadenas
    def __eq__(self, otra):
        if len(self) == len(otra):
            return True
        else:
            return False
