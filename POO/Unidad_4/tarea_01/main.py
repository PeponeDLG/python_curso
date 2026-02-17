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
                        menus.titulo("Listar libros")
                        bibli.mostrar()
                    case "2":
                        menus.titulo("Agregar libro")
                        libro = menus.agregar_libro()
                        bibli.agregar(libro) if libro != None else None
                    case "3":
                        menus.titulo("Buscar libro")
                        titulo = input("\nIntroduzca el título: ")
                        bibli.mostrar(titulo)
                    case "4":
                        menus.titulo("Eliminar libro")
                        isbn = menus.libro_ibn()
                        bibli.eliminar(isbn)
                    case "5":
                        menus.titulo("Prestar libro")
                        isbn = menus.libro_ibn()
                        bibli.disponibilidad_libro(isbn, False)
                    case "6":
                        menus.titulo("Devolver libro")
                        isbn = menus.libro_ibn()
                        bibli.disponibilidad_libro(isbn, True)

if __name__=="__main__":
    Main.main()