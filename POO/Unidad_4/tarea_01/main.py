import menus 
import bbdd_biblioteca as biblio

class Main():
    @staticmethod
    def main():
        opc = int
        bibli = biblio.Biblioteca()
                
        
        while opc != "7":
            opc = menus.menuPrincipal()
            
            if opc == 0:
                input("¡Debe escoger una opción correcta!")
            else:
                match opc:
                    case "1":
                        bibli.mostrar()
                    case "2":
                        libro = menus.agregar_libro()
                        bibli.agregar(libro)
                    case "3":
                        titulo = input("\nIntroduzca el título: ")
                        bibli.mostrar(titulo)
                    




if __name__=="__main__":
    Main.main()