from clase_password import Password
from clase_strong_password import Strong_password

class Main:
    @staticmethod
    def main():
        # Instancia sin parámetro (se genera una contraseña aleatoria)
        # password_1 = Password()
        # print(password_1)
        # print("-"*100)

        # Instancia con contraseña definida por parámetro
        # Probar una más pequeña o algo que no sea una cadena para lanzar excepción
        # password_2 = Password("abcdabcd")
        # print(password_2)
        # print("-"*100)

        # password_1 = Strong_password()
        # print(password_1)
        # print(password_1.es_fuerte())

        passwords = []
        strong_passwords = []

        try:
            # Registra 5 contraseñas simples y si son fuertes o no
            for i in range(1, 6):
                array = []
                print(f"Contraseña simple {i}")
                p = Password()
                fuerza = p.es_fuerte()
                array.append(p)
                array.append(fuerza)
                passwords.append(array)

            # Registra 5 contraseñas fuertes y si son de verdad fuertes o no
            for i in range(1, 6):
                array = []
                print(f"Contraseña fuerte {i}")
                p = Strong_password()
                fuerza = p.es_fuerte()
                array.append(p)
                array.append(fuerza)
                strong_passwords.append(array)

            # Muestra la matriz de contraseñas simples
            print("-"*100)
            print("--- Lista de contraseñas simples ---")
            print("Contraseña | ¿Es fuerte? (True/False)")
            for i in range(5):
                print(f"{passwords[i][0].get_passwd} | {passwords[i][1]}")

            # Muestra la matriz de contraseñas fuertes
            print("-"*100)
            print("--- Lista de contraseñas fuertes ---")
            print("Contraseña | ¿Es fuerte? (True/False)")
            for i in range(5):
                print(f"{strong_passwords[i][0].get_passwd} | {strong_passwords[i][1]}")

        except Exception as e:
            print(e)

if __name__ == "__main__":
    Main.main()
