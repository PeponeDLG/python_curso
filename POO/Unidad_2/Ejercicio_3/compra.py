class Producto:
    def __init__(self,nombre:str, precio:float):
        self.nombre = nombre
        self.precio = precio
    
class Carrito:
    __num_carrito = 0        

    def __init__(self):
        self.productos = []
        Carrito.__num_carrito += 1
        self.num_carrito = Carrito.__num_carrito

    def __eq__():
        pass
        
    def agregar_producto(self, producto: Producto, unidades: int=1):
        if unidades <= 0:
            raise Exception ("El número de unidades no puede ser menor de 1")
        
        for i in range(0,unidades):
            self.productos.append(producto)


    def eliminar_producto(self, producto:Producto, unidades:int=1):
        try:
            if unidades <= 0:
                raise Exception ("El número de unidades no puede ser menor de 1")
            
            self.productos.sort(lambda prod: producto.nombre)

            for i in range(0,unidades):
                if self.productos.count(producto) > 0:
                    self.productos.remove(producto)

        except Exception as e:
            print("ERROR: ",e)

    def vaciar(self):
        self.productos = []


    def total(self):
        precio_total = 0

        for producto in self.productos:
            precio_total += producto.precio

        print("Totall ",self.num_carrito,": ",precio_total)
    
    def listar(self):
        lista = []
        cantidad = 0
        
        self.productos.sort(key=lambda producto : producto.nombre)

        articulo = str
       
        for producto in self.productos:          

            if articulo == producto.nombre:
                lista[-1][1] += 1
            else:
                articulo = producto.nombre
                cantidad = 1                
                lista.append([producto,cantidad])

        lista = map(lambda x: x,"----",lista)

        if len(lista) > 0:
            print("Carrito: nº",self.num_carrito)
            for producto, cantidad_ in lista:
                print("- ",producto.nombre," x ",cantidad_,"(Precio Unidad: ",producto.precio,") -> Precio Subtotal: ",str(cantidad_*producto.precio))


