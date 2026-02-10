from clase_producto import Producto
from clase_carrito import Carrito

class Main:
    @staticmethod
    def main():
        try:
            p1 = Producto("Mortadela", 2)
            p2 = Producto("Salchicha", 4)
            p3 = Producto("Solomillo", 3)
            
            carrito1 = Carrito("Carrito 1")

            # Añado los productos de esta manera para no tener que cambiar la lógica del método
            carrito1.agregar(p1.get_nombre, p1.get_precio)
            carrito1.agregar(p2.get_nombre, p2.get_precio)
            carrito1.agregar(p1.get_nombre, p1.get_precio)
            carrito1.agregar(p3.get_nombre, p3.get_precio)
            carrito1.agregar(p1.get_nombre, p1.get_precio)
            carrito1.agregar(p1.get_nombre, p1.get_precio)
            carrito1.agregar(p2.get_nombre, p2.get_precio)
            carrito1.agregar(p1.get_nombre, p1.get_precio)
            carrito1.agregar(p3.get_nombre, p3.get_precio)

            print("-"*100)
            carrito1.listar()
            print(f"Total: {carrito1.total()} €")

            print("-"*100)
            carrito1.vaciar()
            carrito1.agregar(p1.get_nombre, p1.get_precio)
            carrito1.agregar(p2.get_nombre, p2.get_precio)
            carrito1.agregar(p3.get_nombre, p3.get_precio)

            carrito1.listar()
            print(f"Total: {carrito1.total()} €")


        except Exception as e:
            print(e)
        
if __name__ == "__main__":
    Main.main()
