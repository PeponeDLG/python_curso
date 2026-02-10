class Cadena():
    
    def __init__(self, cadena):
        self.cadena = cadena
        self.vocales = ('a','e','i','o','u','á','é','í','ó','ú')

    def __str__(self):
        return self.cadena

    def __add__(self, x):
        return self.cadena + x.cadena

    def __sub__(self, x):
        for a in x.cadena:
            if a in self.vocales:
                self.cadena = self.cadena.replace(a,"")

        return self.cadena
    
    def __len__(self):
        cont = 0

        for i in self.cadena:
            if i.lower() in self.vocales:               
                cont +=1

        return cont

    def __eq__(self, x):
        
        if len(self) == len(x):
            return True
        else:
            return False

    def __iadd__(self, x):
        return self.cadena + x