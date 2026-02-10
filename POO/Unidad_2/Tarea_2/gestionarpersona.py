from icrud import ICrud
import persona as p


class GestionarPersona(ICrud):

    lPersonas = []

    def Create(self, nombre: str, apellidos: str, correo: str):
        persona = p.persona(nombre, apellidos, correo)
        self.lPersonas.append(persona)

    def Read(self, correo):
        result = [p for p in self.lPersonas if p.correo == correo]

    def Delete(self, correo):
        for i in range(0,len(self.lPersonas)):
            if self.lPersonas[i].correo == correo:
                self.lPersonas.pop(i)
                break

    def Update(self,correo, nombre):
        for i in range(0,len(self.lPersonas)):
            if correo == self.lPersonas[i].correo:
                self.lPersonas[i].nombre = nombre
                
    def Mostrar(self):
        for p in self.lPersonas:
            print(p.nombre, p.apellidos, p.correo)