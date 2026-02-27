from conn_almacen import Conn_almacen
import os

os.system("clear")
    
class Main():
    @staticmethod
    def main():
        conn = Conn_almacen.get_conexion()
        
        try:
            if conn:
                cur = conn.cursor()
                cod_producto = "S10_4757"
                cur.execute(f"""
                            select p.codigoProducto , p.nombreProducto ,p.categoriaProducto, c.descripcion , p.unidadesStock 
                            from productos p
                            left join categoriasproductos c on c.categoria = p.categoriaProducto 
                            where p.codigoProducto = '{cod_producto}';
                            """)
                resq = cur.fetchall()
                
                
                
                for i in resq:
                    for j in i:
                        print(f"-> S{j}")
                
                
                
            else:
                raise Exception("No se ha podido establecer conexión con la BBDD")
            
        except Exception as e:
            print("Error: ",e)
    
if __name__=="__main__":
    os.system("clear")
    Main.main()