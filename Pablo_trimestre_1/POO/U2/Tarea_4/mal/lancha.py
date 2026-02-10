from embarcacion import Embarcacion

class Lancha(Embarcacion):
    # Constantes públicas de clase
    MIN_MOTORES = 1
    MAX_MOTORES = 2
    MIN_COMBUSTIBLE = 8
    MAX_COMBUSTIBLE = 50
    FACTOR_COMBUSTIBLE = 0.026
    MIN_VELOCIDAD_LANCHA = 1
    MAX_VELOCIDAD_LANCHA = 50
    
    # Atributos de clase
    __num_lanchas = 0

    def __init__(self, num_motores:int, combustible:int):
        self.num_motores = num_motores
        self.combustible = combustible

        # Constantes
        self.__min_motores = Lancha.MIN_MOTORES
        self.__max_motores = Lancha.MAX_MOTORES
        self.__min_combustible = Lancha.MAX_COMBUSTIBLE
        self.__factor_combustible = Lancha.FACTOR_COMBUSTIBLE
        self.__min_velocidad_lancha = Lancha.MIN_VELOCIDAD_LANCHA
        self.__max_velocidad_lancha = Lancha.MAX_VELOCIDAD_LANCHA

        Lancha.__num_lanchas += 1
    
    # CONSTANTES
    @property
    def get_num_motores(self):
        return self.num_motores
    
    @property
    def get_combustible(self):
        return self.combustible
    
    #Getters de clase
    @classmethod
    def get_num_lanchas(cls):
        return cls.__num_lanchas
    
    @classmethod
    def __min_motores(cls):
        return cls.MIN_MOTORES
    
    @classmethod
    def __max_motores(cls):
        return cls.MAX_MOTORES
    
    @classmethod
    def __min_combustible(cls):
        return cls.MIN_COMBUSTIBLE
    
    @classmethod
    def __factor_combustible(cls):
        return cls.FACTOR_COMBUSTIBLE
        
    @classmethod
    def __min_velocidad_lancha(cls):
        return cls.MIN_VELOCIDAD_LANCHA
    
    @classmethod
    def __max_velocidad_lancha(cls):
        return cls.MAX_VELOCIDAD_LANCHA
    