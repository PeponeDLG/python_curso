import os

class GestionArchivo():
    @staticmethod
    def buscar(archivo:str, cadena:str) -> bool:
        lista = GestionArchivo.abrir_fichero(archivo)
        
        for linea in lista:
            if linea.__contains__(cadena):
                return True
        
        return False

    @staticmethod
    def contar(archivo:str, cadena:str) -> bool:
        lista = GestionArchivo.abrir_fichero(archivo)
        cont = 0

        for linea in lista:
            cont += linea.count(cadena)
        
        return cont

    @staticmethod
    def mostrar(archivo:str, cadena:str) -> bool:
        lista = GestionArchivo.abrir_fichero(archivo)
        lista_out = []
        nlinea = 0
        cont = 0

        for linea in lista:            
            if linea.__contains__(cadena):
                # lista_out.append(str(str(nlinea) + ":" + str(linea)))
                lista_out.append(f"{nlinea}:{linea}")
            nlinea += 1
        
        return lista_out

    def abrir_fichero(ruta:str) -> []:
        with open(ruta,"r",encoding="UTF-8") as txt:
            return txt.readlines()