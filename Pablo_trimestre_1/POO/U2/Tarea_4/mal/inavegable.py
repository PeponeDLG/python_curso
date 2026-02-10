from abc import ABC, abstractmethod

class INavegable(ABC):
    @abstractmethod
    def iniciar_navegacion(self, velocidad, rumbo, nombre_patron, num_tripulantes):
        pass

    @abstractmethod
    def parar_navegacion(self, tiempo_navegando):
        pass
