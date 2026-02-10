class persona():
    nombre = str
    apellidos = str
    correo = str

    def __init__(self,nombre:str,apellidos:str,correo:str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo