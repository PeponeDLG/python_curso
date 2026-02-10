import random as ran

longMinGLB = 8 

class password:
    password = ""
    longitud = longMinGLB

    # EJERCICIO 1º
    # def __init__(self, longitud: int = longMinGLB, password: str = None):
    #     if password is not None:
    #         self.password = str.strip(password)        
    #         self.longitud = str.count(password)
    #     else:
    #         self.password = ""
    #         self.longitud = longitud

    def __init__(self, longitud: int = longMinGLB):
        self.longitud = longitud

class genera_password(password):

    # def __init__(self, longitud: int = longMinGLB, password: str = None):
    #     super().__init__(longitud,password)

    def __init__(self, longitud: int = longMinGLB):
        super().__init__(longitud)

    def genera_password(self):
        longi = int

        if password is not None and str(password).isspace == False:
            longi = str.count(password)
        else:
            longi = self.longitud

        i = 0
        aux = chr

        while i < longi:
            sel = ran.randint(1,3)

            match sel:
                case 1:            
                    aux = chr(ran.randint(97, 122))
                case 2:            
                    aux = chr(ran.randint(65, 90))
                case 3:            
                    aux = chr(ran.randint(48, 57))

            if aux.isalnum():
                self.password = self.password + str(aux)
                i += 1        
    
    def es_fuerte(self):
        esFuerte = False

        if str.__len__(self.password) > 10:
            mayus = 0
            minus = 0

            for caracter in self.password:
                if caracter.islower():
                    minus += 1
                elif caracter.isupper():
                    mayus += 1
            if minus > 1 and mayus > 2:
                esFuerte = True
            
        return esFuerte


    def __str__(self):
        return f"Contraseña {self.password} con longitud {self.longitud}"