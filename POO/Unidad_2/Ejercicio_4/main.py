from vehículos import *

if __name__=="__main__":
    moto1 = Moto("honda","cb650r","2021")
    
    coche1 = Coche("ford","focus","2007")

    camion1 = Camion("pegasus","A","1973")

    print(moto1)
    print("---------------------------------")
    print(coche1)
    print("---------------------------------")
    print(camion1)
    print("\n--- --- --- --- --- --- --- ---\n")

    moto1.arrancar()
    coche1.arrancar()
    coche1.arrancar()
    print("\n--- --- --- --- --- --- --- ---\n")
    moto1.detener()
    coche1.detener()
    coche1.detener()
