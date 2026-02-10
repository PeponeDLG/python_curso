import os
import csv
import json
from clase import *

def ejercicio1():
    path = os.path.join(os.path.dirname(__file__), "archivos/departaments.csv")

    with open(path, mode="r", encoding="utf8") as fichero:
        fichero_csv = csv.reader(fichero, delimiter=",")

        next(fichero_csv)
        cont = 0

        for l1, l2, l3, l4 in fichero_csv:
            print(f"{l1} - {l2} - {l3} - {l4}")
            cont += 1

        print("Nº Líneas: ", cont)


def ejercicio2():

    pais = "ESP"
    año = "1900"

    path = os.path.join(os.path.dirname(__file__), "archivos/Summer_olympic_Medals.csv")
    list_res = []

    with open(path, mode="r", encoding="utf8") as fich:
        fich_csv = csv.reader(fich)

        for l in fich_csv:
            aux = Resultado_juego(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7])
            list_res.append(aux)

    gest = Gestion_Juegos(list_res)
    gest.get_data_by_country_code(pais)
    gest.get_medals_by_country_code_year(pais,año)
    gest.generate_csv(pais)

def ejercicio3():
    
    path = os.path.join(os.path.dirname(__file__),"archivos/user_behavior_dataset.csv")

    lista = app_movil.get_csv(path, "Google Pixel 5") # Obtener  un  archivo  csv  con  los  datos  de  ese  archivo  filtrados por tipo de dispositivo, columna “Device Model”. Incluir también las cabeceras.
    # [print(l) for l in lista]

    dic = app_movil.get_dict_num_os(path) # Obtener un diccionario con las parejas tipo de sistema operativo y número de entradas en el archivo.
    print(dic)

    app_movil.get_redux(path) # Obtener un archivo csv sólo con las columnas App Usage Time (min/day) y Gender. Añadir cabeceras. 

def ejercicio4():
    path = os.path.join(os.path.dirname(__file__), "archivos/Summer_olympic_Medals.csv")
    
    with open(path, mode="r", encoding="utf8") as fich:
        fich_csv = csv.reader(fich)
        next(fich_csv)

        listado = list(fich_csv)
        
        get_dict_hist(listado, "Spain", True)


def get_dict_hist(lista:list, pais:str, json_file:bool):
    
    res = dict()

    for i in lista:
        if i[3] == pais:
            res[i[0]] = [i[5], i[6], i[7]]

    if json_file and res.__len__() > 0:
        path = os.path.join(os.path.dirname(__file__), "country_code.json")

        with open(path, 'w', encoding="utf-8") as fic:
            path = os.path.join(os.path.dirname(__file__), "country_code.json")
            json.dump(res, fic, indent=4, ensure_ascii=False)

def ejercicio5():
    ventas = [["tomate", 1000, 1.5], ["lechuga", 500, 0.5], ["cebolla", 300, 0.75], ["tomate", 2000, 1.5], ["lechuga", 1000, 0.5], ["cebolla", 600, 0.75], ["pera", 300, 1.75], ["manzana", 500, 1.25],  
              ["uva", 1000, 2.5], ["uva", 2000, 2.5]]
    aux = str
    res = dict()

    for i in ventas:
        for j in res:
            if i[0] == j:
                peso = float(i[1])/1000 # transformarmos de gramos a kilos
                coste = peso * float(i[2]) # calculamos peso x importe
                res[i[0]] = float(res[i[0]]) + coste # añadimos al importe total
                break
        else:
            res[i[0]] = i[2]
        
    path = os.path.join(os.path.dirname(__file__), "mercado.json")

    with open(path, 'w', encoding="utf-8") as fic:
        path = os.path.join(os.path.dirname(__file__), "mercado.json")
        json.dump(res, fic, indent=4, ensure_ascii=False)

def ejercicio6():
    path = os.path.join(os.path.dirname(__file__), "archivos/people.json")

    with open(path, 'r', encoding="utf-8") as fic:
        datos = json.load(fic)

        for i in datos["people"]:
            print(f"Apellido: {i['firstName']}")
            print(f"Apellido: {i['lastName']}")
            print(f"Género: {i['gender']}")
            print(f"Edad: {i['age']}")
            print(f"DNI: {i['number']}\n")

if __name__ == "__main__":
    os.system("clear")
    # ejercicio1()

    # ejercicio2()
    
    # ejercicio3()

    ejercicio4()

    # ejercicio5()

    # ejercicio6()