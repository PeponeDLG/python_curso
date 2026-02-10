from persona import *
from telefono import *
from informatico import *

class Main:
    @staticmethod
    def main():
      cliente1=Cliente("pepe","soler","email",1,2)
      telefono=Smartphone("xiaomi","android",128)

      tecnico1=TecnicoRedes("pepe","soler",180,42,"c#","redes")



        

if __name__=="__main__":
    Main.main()