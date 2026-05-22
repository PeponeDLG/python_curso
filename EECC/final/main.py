import os

# =============================================================================
# SISTEMA DE GESTIÓN DE INVENTARIO - GRAN SUPERFICIE
# =============================================================================

# -----------------------------------------------------------------------------
# Excepción personalizada
# -----------------------------------------------------------------------------
class ProductoNoEncontradoError(Exception):
    """Excepción lanzada cuando no se encuentra un producto por su ID."""
    pass


# -----------------------------------------------------------------------------
# Datos de ejemplo (inventario inicial)
# -----------------------------------------------------------------------------
inventario = [
    {
        "categoria": "Electrónica",
        "subcategorias": [
            {
                "categoria": "ordenador",
                "productos": [
                    {"id": 1, "nombre": "ordenador X", "precio": 1200, "stock": 5},
                    {"id": 2, "nombre": "ordenador Y", "precio": 900, "stock": 0}
                ]
            },
            {
                "categoria": "tablets",
                "productos": [
                    {"id": 3, "nombre": "Tablet Pro", "precio": 350, "stock": 8}
                ]
            }
        ]
    },
    {
        "categoria": "Hogar",
        "subcategorias": [
            {
                "categoria": "cocina",
                "productos": [
                    {"id": 4, "nombre": "Cafetera", "precio": 80, "stock": 12},
                    {"id": 5, "nombre": "Batidora", "precio": 45, "stock": 3}
                ]
            },
            {
                "categoria": "salón",
                "productos": [
                    {"id": 6, "nombre": "Sofá", "precio": 600, "stock": 2}
                ]
            }
        ]
    },
    {
        "categoria": "Deportes",
        "productos": [
            {"id": 7, "nombre": "Pesas 10kg", "precio": 30, "stock": 20},
            {"id": 8, "nombre": "Esterilla Yoga", "precio": 25, "stock": 4}
        ]
    }
]


# -----------------------------------------------------------------------------
# Funciones auxiliares de interfaz
# -----------------------------------------------------------------------------
def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo."""
    os.system('clear' if os.name == 'posix' else 'cls')


def pausa():
    """Pausa la ejecución hasta que el usuario pulse Enter."""
    input("\nPulse Enter para continuar...")


def mostrar_titulo(titulo: str):
    """Muestra un título formateado en pantalla."""
    print(f"\n{'=' * 60}")
    print(f"  {titulo}")
    print(f"{'=' * 60}\n")


# -----------------------------------------------------------------------------
# Funciones de validación
# -----------------------------------------------------------------------------
def validar_precio(precio: float) -> bool:
    """Valida que el precio sea un número positivo."""
    return precio >= 0


def validar_stock(stock: int) -> bool:
    """Valida que el stock sea un número entero no negativo."""
    return stock >= 0 and isinstance(stock, int)


def validar_id(id_producto: int) -> bool:
    """Valida que el ID sea un número entero positivo."""
    return id_producto > 0 and isinstance(id_producto, int)


# -----------------------------------------------------------------------------
# Búsqueda recursiva de producto por ID
# -----------------------------------------------------------------------------
def buscar_producto(inventario: list, id_producto: int) -> dict:
    """
    Busca un producto por su ID de forma recursiva.
    
    Caso base 1: Si la categoría tiene productos, los recorre buscando el ID.
    Caso base 2: Si encuentra el ID, devuelve el producto.
    Caso recursivo: Si tiene subcategorías, profundiza en cada una.
    
    Lanza ProductoNoEncontradoError si no se encuentra.
    """
    for elemento in inventario:
        # Caso base: buscar en productos directos de esta categoría
        if "productos" in elemento:
            for producto in elemento["productos"]:
                if producto["id"] == id_producto:
                    return producto

        # Caso recursivo: buscar en subcategorías
        if "subcategorias" in elemento:
            try:
                resultado = buscar_producto(elemento["subcategorias"], id_producto)
                return resultado
            except ProductoNoEncontradoError:
                continue  # Seguir buscando en otras ramas

    # Si llegamos aquí, no se encontró el producto
    raise ProductoNoEncontradoError(f"Producto con ID {id_producto} no encontrado en el inventario.")


# -----------------------------------------------------------------------------
# Valor total del inventario (función recursiva)
# -----------------------------------------------------------------------------
def calcular_valor_total(inventario: list) -> float:
    """
    Calcula el valor monetario total del inventario de forma recursiva.
    Suma (precio * stock) de todos los productos en todas las ramas.
    """
    total = 0.0

    for elemento in inventario:
        # Sumar productos directos de esta categoría
        if "productos" in elemento:
            for producto in elemento["productos"]:
                total += producto["precio"] * producto["stock"]

        # Sumar productos de subcategorías (recursión)
        if "subcategorias" in elemento:
            total += calcular_valor_total(elemento["subcategorias"])

    return total


# -----------------------------------------------------------------------------
# Añadir / Actualizar productos
# -----------------------------------------------------------------------------
def añadir_producto(inventario: list, categoria: str, subcategoria: str,
                    id_producto: int, nombre: str, precio: float, stock: int) -> bool:
    """
    Añade un producto a una categoría/subcategoría específica.
    Si el producto ya existe (mismo ID), actualiza sus datos.
    Si la categoría o subcategoría no existe, la crea.
    """
    # Validaciones
    if not validar_precio(precio):
        print("Error: El precio no puede ser negativo.")
        return False

    if not validar_stock(stock):
        print("Error: El stock debe ser un número entero no negativo.")
        return False

    if not validar_id(id_producto):
        print("Error: El ID debe ser un número entero positivo.")
        return False

    # Buscar la categoría principal
    for cat in inventario:
        if cat["categoria"].lower() == categoria.lower():
            # Categoría encontrada
            if subcategoria:
                # Buscar o crear subcategoría
                return _añadir_en_subcategoria(cat, subcategoria, id_producto, nombre, precio, stock)
            else:
                # Añadir directamente a la categoría
                return _añadir_producto_en_lista(cat, id_producto, nombre, precio, stock)

    # Si no existe la categoría, la creamos
    nueva_categoria = {"categoria": categoria, "productos": []}
    inventario.append(nueva_categoria)

    if subcategoria:
        nueva_categoria["subcategorias"] = [{"categoria": subcategoria, "productos": []}]
        return _añadir_producto_en_lista(nueva_categoria["subcategorias"][0], id_producto, nombre, precio, stock)
    else:
        return _añadir_producto_en_lista(nueva_categoria, id_producto, nombre, precio, stock)


def _añadir_en_subcategoria(categoria: dict, subcategoria: str,
                            id_producto: int, nombre: str, precio: float, stock: int) -> bool:
    """Añade un producto en una subcategoría específica."""
    if "subcategorias" not in categoria:
        categoria["subcategorias"] = []

    for sub in categoria["subcategorias"]:
        if sub["categoria"].lower() == subcategoria.lower():
            return _añadir_producto_en_lista(sub, id_producto, nombre, precio, stock)

    # Crear nueva subcategoría
    nueva_sub = {"categoria": subcategoria, "productos": []}
    categoria["subcategorias"].append(nueva_sub)
    return _añadir_producto_en_lista(nueva_sub, id_producto, nombre, precio, stock)


def _añadir_producto_en_lista(contenedor: dict, id_producto: int,
                              nombre: str, precio: float, stock: int) -> bool:
    """Añade o actualiza un producto en la lista de productos de un contenedor."""
    if "productos" not in contenedor:
        contenedor["productos"] = []

    for producto in contenedor["productos"]:
        if producto["id"] == id_producto:
            # Actualizar producto existente
            producto["nombre"] = nombre
            producto["precio"] = precio
            producto["stock"] = stock
            print(f"Producto ID {id_producto} actualizado correctamente.")
            return True

    # Añadir nuevo producto
    contenedor["productos"].append({
        "id": id_producto,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    })
    print(f"Producto '{nombre}' (ID: {id_producto}) añadido correctamente.")
    return True


# -----------------------------------------------------------------------------
# Procesamiento de datos con map y filter
# -----------------------------------------------------------------------------
def informe_stock_critico(inventario: list, limite: int = 5) -> list:
    """
    Genera un informe de productos con stock por debajo del límite usando filter.
    Devuelve una lista plana de productos críticos.
    """
    productos_criticos = []

    def extraer_productos(elementos):
        """Función auxiliar recursiva para extraer todos los productos planos."""
        for elem in elementos:
            if "productos" in elem:
                for prod in elem["productos"]:
                    productos_criticos.append(prod)
            if "subcategorias" in elem:
                extraer_productos(elem["subcategorias"])

    extraer_productos(inventario)

    # Usar filter para obtener los que tienen stock < limite
    return list(filter(lambda p: p["stock"] < limite, productos_criticos))


def aplicar_descuento(productos: list, porcentaje: float) -> list:
    """
    Aplica un descuento porcentual a una lista de productos usando map.
    No muta los datos originales, devuelve una nueva lista.
    """
    return list(map(
        lambda p: {
            "id": p["id"],
            "nombre": p["nombre"],
            "precio_original": p["precio"],
            "precio_descuento": round(p["precio"] * (1 - porcentaje / 100), 2),
            "stock": p["stock"]
        },
        productos
    ))


# -----------------------------------------------------------------------------
# Visualización del inventario
# -----------------------------------------------------------------------------
def mostrar_inventario(inventario: list, nivel: int = 0):
    """Muestra el inventario completo de forma jerárquica."""
    sangria = "  " * nivel

    for elemento in inventario:
        print(f"{sangria}📁 {elemento['categoria'].upper()}")

        if "productos" in elemento and len(elemento["productos"]) > 0:
            for prod in elemento["productos"]:
                estado_stock = "⚠️" if prod["stock"] < 5 else "✅"
                print(f"{sangria}  {estado_stock} ID:{prod['id']:3d} | "
                      f"{prod['nombre']:20s} | "
                      f"{prod['precio']:>6.2f}€ | "
                      f"Stock: {prod['stock']:3d}")

        if "subcategorias" in elemento:
            mostrar_inventario(elemento["subcategorias"], nivel + 1)


# -----------------------------------------------------------------------------
# Menú principal
# -----------------------------------------------------------------------------
def menu_principal():
    """Ciclo de vida del menú principal de la aplicación."""
    salir = False

    while not salir:
        limpiar_pantalla()
        mostrar_titulo("SISTEMA DE GESTIÓN DE INVENTARIO")

        print("1.  Mostrar inventario completo")
        print("2.  Buscar producto por ID (búsqueda recursiva)")
        print("3.  Añadir / Actualizar producto")
        print("4.  Calcular valor total del inventario (recursivo)")
        print("5.  Informe de stock crítico (filter)")
        print("6.  Aplicar descuento a productos (map)")
        print("7.  Salir")
        print(f"\n{'=' * 60}")

        opcion = input("\nSeleccione una opción (1-7): ")

        match opcion:
            case "1":
                opcion_mostrar_inventario()
            case "2":
                opcion_buscar_producto()
            case "3":
                opcion_añadir_producto()
            case "4":
                opcion_valor_total()
            case "5":
                opcion_informe_critico()
            case "6":
                opcion_aplicar_descuento()
            case "7":
                salir = True
                print("\nGracias por usar el sistema de gestión de inventario. ¡Hasta pronto!")
                pausa()
            case _:
                print("\nOpción no válida. Intente de nuevo.")
                pausa()


# -----------------------------------------------------------------------------
# Opciones del menú
# -----------------------------------------------------------------------------
def opcion_mostrar_inventario():
    """Muestra el inventario completo."""
    limpiar_pantalla()
    mostrar_titulo("INVENTARIO COMPLETO")
    mostrar_inventario(inventario)
    pausa()


def opcion_buscar_producto():
    """Busca un producto por ID usando búsqueda recursiva."""
    limpiar_pantalla()
    mostrar_titulo("BÚSQUEDA DE PRODUCTO POR ID")

    try:
        id_producto = int(input("Introduzca el ID del producto a buscar: "))

        if not validar_id(id_producto):
            print("Error: El ID debe ser un número entero positivo.")
            pausa()
            return

        producto = buscar_producto(inventario, id_producto)

        print(f"\nProducto encontrado:")
        print(f"  ID:     {producto['id']}")
        print(f"  Nombre: {producto['nombre']}")
        print(f"  Precio: {producto['precio']:.2f}€")
        print(f"  Stock:  {producto['stock']} unidades")

    except ValueError:
        print("\nError: Debe introducir un número entero válido.")
    except ProductoNoEncontradoError as e:
        print(f"\n{e}")

    pausa()


def opcion_añadir_producto():
    """Añade o actualiza un producto en el inventario."""
    limpiar_pantalla()
    mostrar_titulo("AÑADIR / ACTUALIZAR PRODUCTO")

    try:
        categoria = input("Categoría (ej: Electrónica, Hogar, Deportes...): ").strip()
        if not categoria:
            print("Error: La categoría no puede estar vacía.")
            pausa()
            return

        subcategoria = input("Subcategoría (dejar vacío si no tiene): ").strip()

        id_producto = int(input("ID del producto: "))
        nombre = input("Nombre del producto: ").strip()

        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            pausa()
            return

        precio = float(input("Precio (€): "))
        stock = int(input("Stock (unidades): "))

        añadir_producto(inventario, categoria, subcategoria, id_producto, nombre, precio, stock)

    except ValueError:
        print("\nError: Formato de datos incorrecto. Asegúrese de introducir números válidos.")

    pausa()


def opcion_valor_total():
    """Calcula y muestra el valor total del inventario."""
    limpiar_pantalla()
    mostrar_titulo("VALOR TOTAL DEL INVENTARIO")

    total = calcular_valor_total(inventario)
    print(f"El valor monetario total del inventario es: {total:.2f}€")
    pausa()


def opcion_informe_critico():
    """Muestra informe de productos con stock crítico usando filter."""
    limpiar_pantalla()
    mostrar_titulo("INFORME DE STOCK CRÍTICO (filter)")

    try:
        limite = int(input("Introduzca el límite de stock para considerar crítico (por defecto 5): ") or "5")

        criticos = informe_stock_critico(inventario, limite)

        if len(criticos) > 0:
            print(f"\nProductos con stock inferior a {limite} unidades:\n")
            print(f"{'ID':>4s} | {'Nombre':20s} | {'Precio':>8s} | {'Stock':>5s}")
            print("-" * 45)
            for p in criticos:
                print(f"{p['id']:4d} | {p['nombre']:20s} | {p['precio']:8.2f}€ | {p['stock']:5d}")
        else:
            print(f"\nNo hay productos con stock inferior a {limite} unidades.")

    except ValueError:
        print("\nError: Debe introducir un número entero válido.")

    pausa()


def opcion_aplicar_descuento():
    """Aplica un descuento a los productos usando map."""
    limpiar_pantalla()
    mostrar_titulo("APLICAR DESCUENTO A PRODUCTOS (map)")

    try:
        porcentaje = float(input("Introduzca el porcentaje de descuento (ej: 10 para 10%): "))

        if porcentaje < 0 or porcentaje > 100:
            print("Error: El porcentaje debe estar entre 0 y 100.")
            pausa()
            return

        # Extraer todos los productos planos
        todos_productos = []
        def extraer_todos(elementos):
            for elem in elementos:
                if "productos" in elem:
                    todos_productos.extend(elem["productos"])
                if "subcategorias" in elem:
                    extraer_todos(elem["subcategorias"])

        extraer_todos(inventario)

        # Aplicar descuento con map (sin mutar originales)
        productos_descuento = aplicar_descuento(todos_productos, porcentaje)

        print(f"\nProductos con {porcentaje}% de descuento aplicado:\n")
        print(f"{'ID':>4s} | {'Nombre':20s} | {'Precio Original':>15s} | {'Precio Final':>12s} | {'Stock':>5s}")
        print("-" * 65)
        for p in productos_descuento:
            print(f"{p['id']:4d} | {p['nombre']:20s} | "
                  f"{p['precio_original']:8.2f}€      | "
                  f"{p['precio_descuento']:8.2f}€    | "
                  f"{p['stock']:5d}")

    except ValueError:
        print("\nError: Debe introducir un número válido.")

    pausa()


# -----------------------------------------------------------------------------
# Punto de entrada
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario. ¡Hasta pronto!")
    except Exception as e:
        print(f"\nError inesperado: {e}")
