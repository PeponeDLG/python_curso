import pymysql
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

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
                
    def query(self) -> list:
        try:
            cur = self.__conexion.cursor()
            cur.execute("""select c.numeroCliente , CONCAT(c.apellido, ', ' ,c.nombre ), c.telefono ,c.correo 
                            from clientes c order by c.apellido ,c.nombre;""")
            tup = cur.fetchall()
            
            lista = list()
            
            for i in tup:
                lista_aux = [f"Nº Cliente: {i[0]}", f"Nombre: {i[1]}", f"Tlf: {i[2]}", f"E-mail: {i[3]}"]
                lista.append(lista_aux)
                
            return lista            
            
        except Exception as e:
            print("Error query(): ",e)
    
    def pdf_generator(self,lista:list, nombre:str):
        
        try:
            if nombre == "" or nombre.endswith("pdf"):
                raise Exception("El nombre del fichero es obligatorio (sin extensión)")
            
            nombre = os.path.join(os.path.dirname(__file__),nombre+".pfd")
            
            doc = SimpleDocTemplate(f"{nombre}.pdf", pagesize=letter)
            styles = getSampleStyleSheet()
            
            contenido = []
            
            titulo = Paragraph("Listado de clientes", styles['Title'])
            contenido.append(titulo)
            contenido.append(Spacer(1, 12))
            
            for cliente in lista:  # cliente es ["Nº Cliente: 113", "Nombre:...", ...]
                for campo in cliente:  # cada campo es un string
                    p = Paragraph(campo, styles['Normal'])
                    contenido.append(p)
                contenido.append(Spacer(1, 6))  # Separador entre clientes
            
            doc.build(contenido)
            
            return True
        
        except Exception as e:
            print("Error: ", e)
            return False