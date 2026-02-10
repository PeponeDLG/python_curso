from clase_producto import Producto

class Main:
    @staticmethod
    def main():
        # Instancia dos objetos
        producto_1 = Producto(1, "Pelota", "Deportes", 20, 54, 10)
        producto_2 = Producto(2, "Teclado", "Electronica", 30, 14, 5)
        print("-"*100) # Separador visual

        # Imprime ambos objetos
        print(producto_1) # Ejecuta el __str__ de manera implícita
        print(producto_2)
        print("-"*100)

        # Actualiza las unidades del primero
        producto_1.actualizar_stock(50)
        print(producto_1)
        print("-"*100)

        # Comprueba si el segundo está en mínimos
        print(f"¿Stock por debajo del mínimo? {producto_2.esta_en_minimos()}")
        print("-"*100)

        # Comprueba si son iguales
        print(f"¿Son iguales? {producto_1 == producto_2}") # Ejecuta el __eq__ de manera implícita

        print(producto_1.get_categoria) # Para probar el getter (@property permite omitir los () en el .get_categoria)

if __name__ == "__main__":
    Main.main()
