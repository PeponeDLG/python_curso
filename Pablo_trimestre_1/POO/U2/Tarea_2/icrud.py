# Interface. En Python las interfaces simplemente son clases abstractas sin constructor
from abc import ABC, abstractmethod

class ICrud(ABC):
    # Crea una persona nueva
    @abstractmethod
    def create(self, persona):
        pass

    # Busca una persona por su correo
    @abstractmethod
    def read(self, correo):
        pass

    # Elimina una persona de la que se conoce el correo
    @abstractmethod
    def delete(self, correo):
        pass

    # Actualiza el nombre de persona de la que se conoce el correo
    @abstractmethod
    def update(self, correo, nuevo_nombre):
        pass

    # Muestra el contenido de la lista
    @abstractmethod
    def show(self):
        pass
