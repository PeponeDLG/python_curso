from clase_velero import Velero

class Main:
    @staticmethod
    def main():
        # Comienzo de la ejecución

        # -- Programa principal --
        try:
            print("     -- INICIO DEL TEST --")
            print("-"*100)
            
            # 1.- Crea un velero velero1 con 2 mástiles y 5 tripulantes
            velero1 = Velero("El Califa de Cantarranas", 1, 5)

            # 2.- Crea 3 veleros utilizando el método fábrica que se pide en la tarea.
            # Muestra los datos de esos veleros por pantalla.
            velero2 = Velero()
            velero3 = Velero()
            velero4 = Velero()
            print(velero2)
            print(velero3)
            print(velero4)
            print("-"*100)

            # 3.- Inicia la navegación del velero1, muestra sus datos.
            velero1.iniciar_navegacion(20, "ceñida", "Chanquete", 3)
            print(velero1)
            print("-"*100)

            # 4.- Cambia el rumbo del velero1 a "empopada".
            # Muestra si el velero ha cambiado de rumbo.
            velero1.set_rumbo("empopada")
            print(velero1)
            print("-"*100)

            # 5.- Muestra una prueba de los métodos de consulta (Métodos getters).
            # Atributos de instancia
            print(f"    -- Atributos del velero {velero1.get_nombre_barco} --")
            print(f"Nombre: {velero1.get_nombre_barco}")
            print(f"Número de mástiles: {velero1.get_num_mastiles}")
            print(f"Número máximo de tripulantes: {velero1.get_num_max_tripulantes}")
            print(f"Navegando: {velero1.is_navegando}")
            print(f"Tiempo total de navegación: {velero1.get_tiempo_total_navegacion_barco}")
            print(f"Velocidad actual: {velero1.get_velocidad}")
            print(f"Rumbo: {velero1.get_rumbo}")
            print(f"Número de tripulantes: {velero1.get_tripulacion}")
            # Atributos de clase
            print("     -- Atributos genéricos de la clase Velero --")
            clase = Velero()    # Evita el típico problema de 'bound method' de Python
            print(f"Número total de veleros navegando: {clase.get_num_barcos_navegando()}")
            print(f"Número total de veleros creados: {clase.get_num_barcos()}")
            print(f"Tiempo global de navegación de todos los veleros: {clase.get_tiempo_global_navegacion()}")
            print("-"*100)

            # 6.- Para la navegación del velero1.
            # Muestra el tiempo total de la navegación de velero1.
            velero1.parar_navegacion(150)
            print(f"Tiempo total de navegación de {velero1.get_nombre_barco}: {velero1.formatear_tiempo(velero1.get_tiempo_total_navegacion_barco)} horas.")
            print("-"*100)

            # 7.- Crea un nuevo velero e inicia una regata con velero1.
            # Muestra el resultado de la regata.
            velero1.iniciar_navegacion(20, "ceñida", "Chanquete", 2)
            velero2 = Velero("Lentín", 1, 3)
            velero2.iniciar_navegacion(5, "ceñida", "Fantasma de Karol Wojtyla", 2)
            print(velero1.iniciar_regata(velero2))
            print("-"*100)

            # 8.- Muestra de nuevo el tiempo total de la navegación de velero1
            velero1.parar_navegacion(560)
            print(f"Tiempo total de navegación de {velero1.get_nombre_barco}: {velero1.formatear_tiempo(velero1.get_tiempo_total_navegacion_barco)} horas.")
            print("-"*100)
            print("     -- FIN DEL TEST --")
        except Exception as e:  # Lanza la excepción oportuna de las definidas en la clase Velero
            print(e)

        # Fin de la ejecución

if __name__ == "__main__":
    Main.main()
