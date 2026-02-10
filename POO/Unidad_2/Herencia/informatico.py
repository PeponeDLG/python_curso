class Persona:
    def __init__(self, nombre, apellidos, altura, edad):
        self._nombre = nombre
        self._apellidos = apellidos
        self._altura = altura
        self._edad = edad

    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"
    
    def __str__(self):
        return f"{self._nombre} - {self._apellidos} - {self._altura} - {self._edad}"
    

# Herencia simple de la clase Persona a la clase Informatico
class Informatico(Persona):
    def __init__(self, nombre, apellidos, altura, edad, lenguaje):
        super().__init__(nombre, apellidos, altura, edad)
        self._lenguajes= ['Python'] # Lenguajes que domina, por defecto Python 
        self._experiencia = 1  # Años de experiencia
    
    def insertarLenguajes(self, lenguaje, experiencia=1):
        if lenguaje not in self._lenguajes:
            self._lenguajes.append(lenguaje)
            if experiencia > 0:
                self._experiencia += experiencia # Añadimos experiencia en todos los lenguajes
            else:
                raise ValueError("La experiencia debe ser mayor que 0")
        else:
            raise ValueError(f"El lenguaje {lenguaje} ya lo domina")
        
        return self._lenguajes

    def programar(self):
        return "Estoy programando"
    
    def __str__(self):
        return f"{self._nombre} - {self._apellidos} - {self._altura} - {self._edad} - {",".join(self._lenguajes)} - {self._experiencia} años de experiencia"

# Herencia de la clase Informatico a la clase TecnicoRedes
class TecnicoRedes(Informatico):
    def __init__(self, nombre, apellidos, altura, edad, lenguaje, especialidad):
        super().__init__(nombre, apellidos, altura, edad, lenguaje)
        self._especialidad = especialidad
    
    def __str__(self):
        return super().__str__() + f"{self._especialidad}"