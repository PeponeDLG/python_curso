import os
from pymysql import connect, MySQLError

os.system('clear' if os.name == 'posix' else 'cls')

def query(codProucto:str, unidades:int):
    try:
        # Establece la conexión con la base de datos MySQL
        with connect(
            host='localhost',
            user='root',
            password='Trassierra2026$',
            port=3309,
            database='almacen'
        ) as conexion:
            # Crea el cursor
            with conexion.cursor() as cursor:
                sql = "select unidadesStock from productos where codigoProducto='"+codProucto+"'"
                # Ejecuta la consulta y devuelve el num. de filas afectadas
                cursor.execute(sql)
                filas = cursor.fetchall()

                if filas.__len__() > 0:
                    sql = f"update productos set unidadesStock={(int(filas[0][0])+unidades)} where codigoProducto='{codProucto}'"
                    res = cursor.execute(sql)
                    if res > 0:
                        conexion.commit()
                    else:
                        conexion.rollback()
                    

                # Recorre los resultados contenidos en el cursor
                # for cliente in cursor.fetchall():
                #     print(cliente)
        
    except MySQLError as e:
        print("Error:", e)

print(query("S12_1099",2))