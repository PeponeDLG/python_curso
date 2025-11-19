# Definición de una clase

class Coche:
     # Atributo de clase (contador de instancias)
    contador = 0

    # Método contructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
        
        
        # Cada vez que se crea un coche, el contador de la clase aumenta en 1
        Coche.contador += 1
    
    def acelerar(self):
        self.velocidad += 5

    def frenar(self):
        self.velocidad -= 5
    
    def getInfo(self):
        info = "------Información del coche------"
        info += f"\nColor: {self.color}\nMarca: {self.marca}\nModelo: {self.modelo}\nVelocidad: {self.velocidad}\nCaballaje: {self.caballaje}\nPlazas: {self.plazas}" 
        return info
    
# fin de la definición de la clase