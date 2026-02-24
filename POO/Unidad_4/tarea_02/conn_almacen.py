import pymysql

class Conn_almacen():
    __conexion = None
    test_conn = str

    @classmethod
    def get_conexion(cls):
        """Devuelve la conexión (la crea si no existe)"""
        try:
            if cls.__conexion is None:
                cls.__conexion = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='Trassierra2026$',
                    port=3309,
                    database='almacen'
                )
                cls.test_conn = "Conexión establecida"
            return cls.__conexion
        except Exception as e:
            print(f"Error al conectar: {e}")
            return None

    @classmethod
    def close_conexion(cls):
        """Cierra la conexión si existe"""
        try:
            if cls.__conexion is not None:
                cls.__conexion.close()
                cls.__conexion = None
                print("Conexión cerrada")
            return True
        except Exception as e:
            print(f"Error al cerrar la conexión: {e}")
            return False