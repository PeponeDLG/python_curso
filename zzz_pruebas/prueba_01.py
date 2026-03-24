import os
import sqlite3 as sql

os.system("clear")

dic = {
    "persona":{
        "nombre":"pepe",
        "apellido1":"soler",
        "apellido2":"membrives"
    },
    "notas":[1,3,2,4,5,6]
}

for i in dic:
    for j in dic[i]:
        print(j)