import os
import sqlite3 as sql

try:
    
    path = os.path.join("./z_BBDD/","POO.db")
    
    # for i in os.listdir("./"):
    #     print(i)
    
    print(os.path.exists(path))
    
    conn = sql.connect(path)

    cur = conn.cursor()
    cur.execute("insert into tabla1 values(1,2)")

    conn.commit()
except sql.Error as e:
    print("Error de conexión: ",e)