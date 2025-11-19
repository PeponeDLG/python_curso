class clasePadre:
    #constantes
    atributo="publico"
    _atributo="protected"
    __atributo="privado"


    def __init__(self,attr1,attr2,attr3):
        self.attr1=attr1
        self.attr2=attr2
        self.attr3=attr3
   
    def metodo1(self):
        print("entra metodo 1")
    
    def metodo2(param1):
        print("metodo2 ->",param1)
    
    metodo2("prueba")

class claseHija(clasePadre):
    def funcion1(self):
        print("pasa por clase 2")
        return

class claseNieta(claseHija):
    def ff(self):
        return 2

if __name__=="__main__":

    clasepadre=clasePadre(1,2,3)
    clasehija=claseHija(4,5,6)
    clasehnieta=claseNieta(7,8,9)
   
    print("clasePadrePublic",clasepadre.atributo)
    print("clasePadreProtected",clasepadre._atributo)
    # print("clasePadrePrivate",clasepadre.__atributo)
    print("")
    print("claseHijaPublic",clasehija.atributo)
    print("claseHijaProtected",clasehija._atributo)
    # print("claseHijaPrivate",clasehija.__atributo)
    print("")
    print("claseNietaPublic",clasehnieta.atributo)
    print("claseNietaProtected",clasehnieta._atributo)
    # print("claseNietaPrivate",clasehnieta.__atributo)