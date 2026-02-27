import os
from pymysql import connect, MySQLError

os.system('clear' if os.name == 'posix' else 'cls')

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
            sql = 'SELECT * FROM clientes'
            # Ejecuta la consulta y devuelve el num. de filas afectadas
            num_filas = cursor.execute(sql)

            # Recorre los resultados contenidos en el cursor
            for cliente in cursor.fetchall():
                print(cliente)
    
except MySQLError as e:
    print("Error:", e)