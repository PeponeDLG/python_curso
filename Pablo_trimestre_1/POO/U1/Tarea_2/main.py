from clase_producto import Producto
from clase_gestion_almacen import GestionAlmacen

class Main:
    @staticmethod
    def main():

        # Llama al método “listado” y muestra los productos existentes.
        GestionAlmacen.listado()
        print("-"*100)

        # Usando el método “nuevo_producto”, añade dos productos nuevos
        # El segundo debe tener el mismo identificador que el primero
        # Comprueba si se añaden los dos o uno solo
        nuevo_1 = Producto(3, "Sombrilla", "Ocio", 15, 37, 4)
        print(f"Producto introducido con éxito: {GestionAlmacen.nuevo_producto(nuevo_1)}")
        nuevo_2 = Producto(3, "Sombrilla", "Ocio", 15, 37, 4)
        print(f"Producto introducido con éxito: {GestionAlmacen.nuevo_producto(nuevo_2)}")
        print("-"*100)

        # Llama al método “bajo_minimos” y guarda en una lista los productos que estén en mínimos
        # Muestra el contenido de la lista
        minimos = GestionAlmacen.bajo_minimos()
        for producto in minimos:
            print(producto)
        print("-"*100)
        
if __name__ == "__main__":
    Main.main()
