# Definición de una clase

class Coche:
     # Atributo de clase (contador de instancias)
    contador = 0
    

    # Método contructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        
        self.color = color # Atributo de instancia
        self.__marca = marca # Atributo privado
        self.__modelo = modelo # Atributo privado
        self._velocidad = velocidad # Atributo protegido
        self._caballaje = caballaje # Atributo protegido
        self._plazas = plazas # Atributo protegido        
        
        # Cada vez que se crea un coche, el contador de la clase aumenta en 1
        Coche.contador += 1
    
    def acelerar(self):
        self.velocidad += 5

    def frenar(self):
        self.velocidad -= 5
    
    def getInfo(self):
        info = "------Información del coche------"
        info += f"\nColor: {self.color}\nMarca: {self.__marca}\nModelo: {self.__modelo}\nVelocidad: {self._velocidad}\nCaballaje: {self._caballaje}\nPlazas: {self._plazas}" 
        return info
    
    # Método de clase para obtener el número de coches creados
    @classmethod
    def get_num_coches(cls):
        return cls.contador
    @staticmethod
    def estatico(a:str=str.sp):
        print("método estático: ",a)
        

# fin de la definción de la clase