from conn_almacen_csv import Conn_almacen
import os

os.system("clear")

class Main():
    @staticmethod
    def main():
        conn = Conn_almacen()
        
        try:
            if conn.test_conn:             
                res = conn.read_csv("clientes.csv")

                if res.__len__() > 0:
                    if conn.insert_clientes(res):
                        conn.list_clientes()
                    else:
                        print("Ha habido un error en la inserción.")
                else:
                    print("No se ha podido leer el listado de clientes CSV.")

            else:
                raise Exception("No se ha podido establecer conexión con la BBDD")
            
        except Exception as e:
            print("Error: ",e)
    
if __name__=="__main__":
    os.system("clear")
    Main.main()