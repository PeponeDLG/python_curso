import os
from pymysql import connect, MySQLError

os.system('clear' if os.name == 'posix' else 'cls')

def query(catego:str):
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
                sql1 = f"delete from productos where categoriaProducto='{catego}'"
                sql2 = f"delete from categoriasproductos where categoria='{catego}'"
                # Ejecuta la consulta y devuelve el num. de filas afectadas
                cursor.execute(sql1)
                cursor.execute(sql2)
                conexion.commit()    

                # Recorre los resultados contenidos en el cursor
                # for cliente in cursor.fetchall():
                #     print(cliente)
        
    except MySQLError as e:
        print("Error:", e)

print(query("ships"))