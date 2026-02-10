from clases import *

class Main:
    @staticmethod
    def main():

        # Se pasa por parámetro un Email vacío, ya que no tiene constructor
        notificador_1 = Notificador(Email())
        notificador_1.notificar("Hola mundo")
        notificador_1.cambiar_canal(Whatsapp())
        notificador_1.notificar("Whatsaaaaaaaaap")

if __name__ == "__main__":
        Main.main()
