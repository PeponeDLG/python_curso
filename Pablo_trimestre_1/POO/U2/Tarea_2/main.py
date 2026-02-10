from persona import Persona
from gestion_persona import GestionPersona
from icrud import ICrud

class Main:
    @staticmethod
    def main():
        try:
            # Crea varias instancias de Persona y una instancia de GestionPersona
            p1 = Persona("Pirri", "Moris", "pirri@moris.com")
            p2 = Persona("Laura", "Perez", "Laura@perez.com")
            p3 = Persona("Javi", "Ramos", "javi@ramos.com")
            p4 = Persona("Leo", "Jimenez", "leo@jimenez.com")
            g1 = GestionPersona()

            # Guarda las instancias de Persona en la lista de GestionPersona (Create)
            g1.create(p1)
            g1.create(p2)
            g1.create(p3)
            g1.create(p4)

            # Busca una Persona en la lista por su correo para mostrarla (Read)
            print(g1.read("pirri@moris.com"))
            print("-"*100)

            # Actualiza el nombre de Persona y la muestra (Update)
            g1.update("pirri@moris.com", "Fulanito")
            print(p1)
            print("-"*100)

            # Busca una Persona en la lista por su correo para eliminarla de la lista (Delete)
            g1.delete("javi@ramos.com")

            # Muestra el contenido de la lista de GestionPersona
            print(g1.show())
            
        except Exception as e:
            print(e)

if __name__ == "__main__":
    Main.main()
