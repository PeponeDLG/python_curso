from clase_producto import Producto

class Carrito:
    def __init__(self, nombre:str):
        self.__lista = []
        self.__nombre = nombre

    # Agrega un producto al carrito
    def agregar(self, nombre:str, precio:float):
        producto = Producto(nombre, precio)
        # Si ya contiene un producto igual aumenta su cantidad en vez de agregarlo
        if producto in self.get_lista:
            for p in self.get_lista:
                if p in self.__lista:
                    p.set_cantidad(p.get_cantidad + 1)
                    break
        else:
            self.get_lista.append(producto)

    # Elimina un producto del carrito
    def eliminar(self, nombre:str):
        for p in self.get_lista:
            if p.get_nombre == nombre:
                # Si hay más de un objeto igual, se reduce su cantidad. Si no, se elimina de la lista.
                if p.get_cantidad > 1:
                    p.set_cantidad(p.get_cantidad - 1)
                    break
                else:
                    self.get_lista.remove(p) # remove() elimina objetos, pop() elimina por índice
                    break
        # Sólo se ejecuta si no se ejecuta el break
        else:
            raise Exception("No hay ningún producto con ese nombre en la cesta.")

    # Elimina todo el contenido de un carrito
    def vaciar(self):
        self.__lista = []

    # Lista el contenido de un carrito
    def listar(self):
        print(f"{self.__nombre}:")
        for p in self.__lista:
            print(f"- {p.get_nombre} x {p.get_cantidad} (Precio Unidad: {p.get_precio}) -> Precio Subtotal: {p.get_precio * p.get_cantidad} €")

    # Devuelve el importe total del carrito
    def total(self):
        total = 0
        for p in self.get_lista:
            total += p.get_precio * p.get_cantidad
        
        return total

    # Getters y setters
    @property
    def get_lista(self):
        return self.__lista

    @classmethod
    def get_num_carritos(cls):
        return cls.__num_carritos
