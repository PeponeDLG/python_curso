import pymysql

try:
    # Establecer conexión con la base de datos
    with pymysql.connect(       # Establece la conexion a la base de datos
        host='localhost',       # Servidor de la base de datos
        user='user',            # Usuario de la base de datos
        password='poo',  # Contraseña de la base de datos
        port=3309,              # Puerto de la base de datos
        database='almacen'      # Nombre de la base de datos
    ) as conexion:              # 

        # Crear un cursor para ejecutar consultas SQL
        with conexion.cursor() as cursor:

            # Ejecución de la consulta
            sql = 'SELECT * FROM clientes'
            numero_filas = cursor.execute(sql) # Ejecuta la consulta y devuelve el número de filas afectadas

            # Recorrer los resultados contenidos en el cursor
            for cliente in cursor.fetchall():
                print(cliente)

except pymysql.MySQLError as e: # Manejo de errores de la base de datos
    print(f'Error en SQL: {e}')