# Clase base 1
class Telefono:
    def llamar(self, numero):
        return f"Llamando al {numero}..."

    def colgar(self):
        return "Llamada finalizada."


# Clase base 2
class Dispositivo:
    def __init__(self, sistema, almacenamiento):
        self.sistema = sistema
        self.almacenamiento = almacenamiento

    def info(self):
        return f"Sistema: {self.sistema}, Almacenamiento: {self.almacenamiento}GB"


# Clase derivada con herencia múltiple
class Smartphone(Telefono, Dispositivo):
    def __init__(self, marca, sistema, almacenamiento):
        # Inicializamos el constructor de Dispositivo
        Dispositivo.__init__(self, sistema, almacenamiento)
        self.marca = marca

    def __str__(self):
        return f"{self.marca} - {self.info()}"