import os
import menus
import pymysql
from libro import Libro

class Biblioteca():
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
                    database='biblioteca'
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
    
    def mostrar(self, titulo="") -> list:
        
        try:
            cur = self.__conexion.cursor()

            if cur != None:
                
                if len(titulo) > 0:
                    cur.execute("select * from libros where titulo=%s", titulo)
                else:
                    cur.execute("select * from libros")
                    
                res = cur.fetchall()
                
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
    
        except Exception as e:
            print("Error: ", e)
            
            
    def agregar(self, libro:Libro):
        try:
            cur = self.__conexion.cursor()

            cur.execute("insert into libros values (%s,%s,%s,%s)",(libro.isbn,libro.titulo,libro.autor,str(libro.disponible)))
            self.__conexion.commit()
            
        except Exception as e:
            print("Error al insertar: ",e)
    
    def eliminar(self, isbn):
        try:
            cur = self.__conexion.cursor()

            cur.execute("delete from libros where isbn=%s",isbn)
            cur.fetchall()
            self.__conexion.commit()
            
        except Exception as e:
            print("Error al eliminar: ",e)

    def disponibilidad_libro(self, isbn, estado):
        try:
            cur = self.__conexion.cursor()
            
            
                       

            cur.execute("select disp from libros where isbn=%s",isbn)
            disp = cur.fetchall()

            if disp.__len__() > 0:
                if estado:
                    if disp[0][0] == 0:
                        estado = 1
                    else:
                        print("El libro ya está devuelto.")
                        input("Pulse enter para continuar...")
                        return False
                else:
                    if disp[0][0] == 1:
                        estado = 0
                    else:
                        print("El libro no está disponible.")
                        input("Pulse enter para continuar...")
                        return False


                cur.execute("update libros set disp=%s where isbn=%s",(estado,isbn))
                cur.fetchall()
                self.__conexion.commit()

                if estado == 0:
                    print("Libro prestado correctamente.")
                    input("Pulse enter para continuar...")
                else:
                    print("Libro devuelto correctamente.")
                    input("Pulse enter para continuar...")

            else:
                print("El libro con ISBN ",isbn," no existe.")
                input("Pulse enter para continuar...")
        except Exception as e:
            print("Error al eliminar: ",e)