from clase_password import Password

class Main:
    @staticmethod
    def main():
        # Comienzo de la ejecución
        
        # Instancia sin parámetro (se genera una contraseña aleatoria)
        password_1 = Password()
        print(password_1)
        print("-"*100)

        # Instancia con contraseña definida por parámetro
        # Probar una más pequeña o algo que no sea una cadena para lanzar excepción
        password_2 = Password("abcdabcd")
        print(password_2)
        print("-"*100)

        # Fin de la ejecución

if __name__ == "__main__":
    Main.main()
