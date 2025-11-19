class Persona:
    # __init__(): se ejecuta al crear un objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Objeto Persona creado: {self.nombre}, {self.edad} años")

    # __str__(): representación para el usuario (informal, legible)
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"
    
    def str(self):
        return f"{self.nombre}, {self.edad} años"

    # __repr__(): representación para el programador (más técnica)
    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

    # __eq__(): permite comparar dos objetos con "=="
    def __eq__(self, otro):
        if isinstance(otro, Persona):
            return self.nombre == otro.nombre and self.edad == otro.edad
        return False

    # __del__(): destructor, llamado cuando se elimina el objeto
    def __del__(self):
        print(f"Objeto Persona eliminado: {self.nombre}")