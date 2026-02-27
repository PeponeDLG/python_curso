from conn_almacen_pdf import Conn_almacen
import os

os.system("clear")

class Main():
    @staticmethod
    def main():
        conn = Conn_almacen()
        
        try:
            if conn.test_conn:
                lista = conn.query()                 
                
                if conn.pdf_generator(lista,"listado_clientes"):
                    print("Listado de clientes generado.")
                else:
                    print("No se ha podido generar el listado de clientes.")

            else:
                raise Exception("No se ha podido establecer conexión con la BBDD")
            
        except Exception as e:
            print("Error: ",e)
    
if __name__=="__main__":
    os.system("clear")
    Main.main()