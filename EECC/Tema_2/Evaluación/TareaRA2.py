import os

"""
Programa que genera un listado de la compra según los productos que falten en la despensa y la nevera.
"""

tiposK = (1, 2, 3, 4, 5)
tiposV = ("Carne", "Pescado", "Fruta", "Verdura", "Otros")


class Producto:
    tipo = int  # 1-Carne, 2-Pescado, 3-Fruta, 4-Verdura, 5-Otros
    nombre = str
    cantidad = int
    comprar = True

    def __init__(self, tipo: int, nombre: str, cantidad: int):
        self.tipo = tipo
        self.nombre = nombre
        self.cantidad = cantidad

        if cantidad == 0:
            self.comprar == True
        else:
            self.comprar == False

    def ajustarCantidad(self, cantidad: int):
        self.cantidad += cantidad


if __name__ == "__main__":

    # Preparación de listado
    pr1 = Producto(1, "Filetes", 3)
    pr2 = Producto(1, "Pollo", 7)

    pr3 = Producto(3, "Naranjas", 10)
    pr4 = Producto(5, "Cerveza", 12)

    lista = [pr1, pr2, pr3, pr4]
    # --- Fin preparación de listado ---

    # --- --- --- --- --- Bloque de definición de funciones --- --- --- --- ---

    # Func: menú principal - Tipos de productos -
    def menuTipo():
        sel = 0

        while sel != "" and sel == 0:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("\nTipos de productos")
            print("__________________\n")

            for i in tiposK:
                print(tiposK[i - 1], " - ", tiposV[i - 1])

            sel = controlMenu(input("\nSeleccione: "), len(tiposK))

        return sel

    # Func: menú productos
    def menuProductos(selTipo, listado):
        sel = 0

        while sel != '' or sel == 0:

            prods = 0
            listaAux = []

            os.system('clear' if os.name == 'posix' else 'cls')
            print("\nProductos")
            print("_________\n")

            for i in listado:
                if i.tipo == selTipo:
                    prods += 1
                    print(prods, "-", i.nombre, "  -> ", i.cantidad, " unid.")
                    listaAux.append(i)

            if len(listaAux) > 0:
                sel = controlMenu(input("\nSeleccione: "), prods)
            
                prods = 0

                for i in listado:
                    if i.tipo == selTipo:
                        prods += 1
                        if prods == sel:
                            return i
            else:
                print(f"No hay productos del tipo {selTipo}...\n")
                input("Presione una tecla para continuar...")
                sel = ''

            

        return sel

    # Func: menú añadir o quitar productos
    def ajustarProductos(produc: Producto):

        sel = 0

        os.system('clear' if os.name == 'posix' else 'cls')
        print("Operación")
        print("_________\n")

        while sel != "" and sel == 0:
            print("1 - Añadir productos")

            if produc.cantidad > 0:
                print("2 - Eliminar productos")

            sel = controlMenu(input("\nSeleccione: "), 2)

        salir = False
        unidades = ""

        while salir == False:
            match sel:
                case 1:
                    unidades = controlMenu(input("\nUnidades a añadir (10max.): "), 10)
                case 2:
                    unidades = controlMenu(
                        input(f"\nUnidades a eliminar ({produc.cantidad}max.): "),
                        produc.cantidad,
                    )

            if unidades != "":
                if unidades > 0:
                    if sel == 1 and unidades <= 10:
                        produc.ajustarCantidad(unidades)
                        salir = True
                    elif sel == 2 and unidades <= produc.cantidad:
                        produc.ajustarCantidad(unidades * -1)
                        salir = True
            elif unidades == "":
                salir = True

    # Control de la entrada por teclado válida en formato y número
    def controlMenu(sel, long):

        if sel.isnumeric() == True:
            aux = int(sel)
            if aux > 0 and aux <= long:
                return aux
        elif sel.isalpha and sel == "":
            return ""

        # Si no cumple los requisitos
        print("\n¡Error! Debe elegir un número entre 1 y ", long, "\n")
        input("Pulse para continuar...\n")
        return 0

    # -- Fin del bloque de definición de funciones

    # -- Menú de usuario --
    exit = False
    tipo = None

    while exit == False:
        if tipo != "":
            tipo = menuTipo()
            if tipo != "":
                producto = menuProductos(tipo, lista)
                if producto != "":
                    ajustarProductos(producto)
        else:
            exit = True
