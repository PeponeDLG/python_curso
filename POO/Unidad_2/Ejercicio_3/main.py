from compra import *

if __name__=="__main__":
    try:
        p1=Producto("Libro",20.3)
        p2=Producto("Disco", 15.89)
        p3=Producto("Bolígrafo", 1.5)

        carrito1 = Carrito()
        carrito2 = Carrito()

        carrito1.agregar_producto(p1,2)
        carrito1.agregar_producto(p2,1)
        carrito1.agregar_producto(p3,5)

        carrito2.agregar_producto(p1,1)
        carrito2.agregar_producto(p2,3)
        carrito2.agregar_producto(p3,1)

        carrito1.listar()
        carrito2.listar()

        print("\n -- -- -- eliminamos un Bolígrafo del carrito 1 -- -- -- \n")

        carrito1.eliminar_producto(p3,6)

        carrito1.listar()
        carrito2.listar()

        print("\n -- -- -- mostramos el precio total -- -- -- \n")

        carrito1.total()
        carrito2.total()

        carrito1.vaciar()

    except Exception as e:
        print(e)