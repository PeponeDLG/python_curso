import pymysql
import csv
import os

class Conn_almacen():
    __conexion = None
    test_conn = False

    def __init__(self):
        try:
            if self.__conexion is None:
                self.__conexion = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='Trassierra2026$',
                    port=3309,
                    database='almacen'
                )
                
                self.test_conn = True            
        except Exception as e:
            print(f"Error al conectar: {e}")

    def close_conexion(self):
        """Cierra la conexión si existe"""
        try:
            if self.__conexion is not None:
                self.__conexion.close()
                self.__conexion = None
                print("Conexión cerrada")
            return True
        except Exception as e:
            print(f"Error al cerrar la conexión: {e}")
            return False
                
    def read_csv(self,nom_fich) -> list:
        try:
            path = os.path.join(os.path.dirname(__file__), nom_fich)
            lista = []

            with open(path, mode="r", encoding="utf8") as fichero:
                fichero_csv = csv.reader(fichero, delimiter=",")

                next(fichero_csv)
                cont = 2

                for l in fichero_csv:
                    if l.__len__() == 5:
                        lista.append(l)
                    else:
                        print("Formato de erróneo en línea: ",cont)
                    cont += 1
                
            return lista            
            
        except Exception as e:
            print("Error query(): ",e)
    
    def insert_clientes(self,lista:list) -> bool:
        
        try:
            cur = self.__conexion.cursor()
            
            inserts = str()

            for l in lista:
                inserts = inserts + (f"({l[0]},'{l[1]}','{l[2]}','{l[3]}','{l[4]}'),")
            
            inserts = "Insert into clientes values " + inserts
            inserts = inserts.removesuffix(",")

            cur.execute(inserts)
            cur.fetchall()
            
            self.__conexion.commit()

            return True
        
        except Exception as e:
            print("Error: ", e)
            return False
        
    def list_clientes(self):
        try:
            cur = self.__conexion.cursor()
            
            cur.execute("select * from clientes")
            lista = cur.fetchall()
            print("\n\n")

            if lista.__len__() > 0:
                for l in lista:
                    print(f"Nº: {l[0]}")
                    print(f"Nombre: {l[1]}")
                    print(f"Apellidos: {l[2]}")
                    print(f"Tlf: {l[3]}")
                    print(f"e-mail: {l[4]}\n---------------\n")


        except Exception as e:
            print("Error: ", e)
            return False