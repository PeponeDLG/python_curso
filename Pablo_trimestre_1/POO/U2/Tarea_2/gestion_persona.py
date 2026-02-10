from icrud import ICrud
from persona import Persona

class GestionPersona(ICrud):
    def __init__(self):
        self.__lista_personas = []

    # Añade una persona a la lista si ésta no existe (buscada por su correo)
    def create(self, persona):
        if not isinstance(persona, Persona):
            raise ValueError("No es una persona")

        if self.read(persona.correo) == None:
            self.__lista_personas.append(persona)
        else:
            raise Exception("Ya existe una persona con ese correo")

    # Busca el correo de una persona en la lista y si lo encuentra devuelve la persona
    def read(self, correo):
        for persona in self.__lista_personas:
            if persona.correo == correo:
                return persona

        return None

    # Elimina una persona de la lista si ésta existe (buscada por su correo)
    def delete(self, correo):
        for persona in self.__lista_personas:
            if persona.correo == correo:
                self.__lista_personas.remove(persona)
                return True

        return None

    # Actualiza el nombre de una persona (buscada por su correo)
    def update(self, correo, nombre):
        for persona in self.__lista_personas:
            if persona.correo == correo:
                persona.nombre = nombre
                return True

        return None

    # Muestra el contenido de la lista
    def deprecated_show(self):
        listado = ""
        for persona in self.__lista_personas:
            listado += str(persona) + "\n" # str() invoca el __str__ de Persona

        return listado

    # Versión pythónica de show() usando join() para devolver una lista formateada en filas
    # Fuente: https://docs.python.org/es/3.14/library/stdtypes.html#str.join
    def show(self):
        return "\n".join(str(persona) for persona in self.__lista_personas)
