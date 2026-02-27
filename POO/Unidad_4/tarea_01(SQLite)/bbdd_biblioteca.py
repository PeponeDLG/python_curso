import os
import menus
import sqlite3 as sql
from libro import Libro

class Biblioteca():
    __CADENA_CONN = "biblioteca.db"
    __CONN = None
    __CUR = None
    
    def __init__(self):
        try:
            path = os.path.join(os.path.dirname(__file__), self.__CADENA_CONN)
            
            if os.path.exists(path):
                self.__CONN = sql.connect(path)
                self.__CUR = self.__CONN.cursor()                
            else:
                raise Exception(f"No se encuentra la BBDD '{self.__CADENA_CONN}'")
            
        
        except sql.Error as e:
            print("Error sqlite3: ", e)
        except Exception as e:
            print("Error: ", e)
    
    
    
    def mostrar(self, titulo="") -> []:
        
        try:
            if self.__CUR != None:
                
                if len(titulo) > 0:
                    self.__CUR.execute("select * from libros where titulo=?", titulo)
                else:
                    self.__CUR.execute("select * from libros")
                    
                res = self.__CUR.fetchall()
                
                if res.__len__() > 0:
                    menus.clear()

                    print("Listado de libros")
                    print("=================\n")
                                        
                    for i in res:
                        if i[3] == 0:
                            print(f"Título: {i[1]}, Autor: {i[2]}, ISBN: {i[0]}, Disponible: No")
                        else:
                            print(f"Título: {i[1]}, Autor: {i[2]}, ISBN: {i[0]}, Disponible: Si")
                            
                    input("\nPulse enter para continuar...")
                else: 
                    print("No existen libros en la biblioteca")
        
        except sql.Error as e:
            print("Error sqlite3: ", e)
        except Exception as e:
            print("Error: ", e)
            
            
    def agregar(self, libro:Libro):
        try:
            self.__CUR.execute("insert into libros values (?,?,?)",(libro.isbn,libro.titulo,libro.autor,libro.disponible))
            self.__CONN.commit()
            
        except sql.Error as e:
            print("Error al insertar: ",e)
        