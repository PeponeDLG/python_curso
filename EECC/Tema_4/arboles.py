import os
os.system("clear")

catalogo = {
    "nombre":"tienda",
    "hijos": [
        {
            "nombre":"perifericos",
            "hijos":[
                {"nombre":"teclado","precio":30.0},
                {"nombre":"raton","precio":15.0},
            ],
        },
        {
            "nombre":"pantallas",
            "hijos":[
                {"nombre":"monitor","precio":130.0},
            ],
        },
        {
            "nombre":"cables",
            "hijos":[
                {"nombre":"hdmi","precio":7}
            ],
        }
    ]
}

def mina_list(cat, g:str):
    for i in cat:
        if type(i) == type(dict()):
            mina(i,i.keys(),f"{g}-")
        elif type(i) == type(list()):
            mina_list(cat[i],f"{g}-")
        else:
            print(f"{g}{cat[i]}")

def mina(cat, items=[], g:str=""):

    for i in cat:
        if type(cat[i]) == type(dict()):
            mina(cat[i],cat[i],f"{g}-")
        elif type(cat[i]) == type(list()):
            mina_list(cat[i],f"{g}-")
        else:
            print(f"{g}{cat[i]}")

mina(catalogo,catalogo.keys(),"/")

