from gestionarpersona import GestionarPersona

if __name__=="__main__":

    listaPersonas = GestionarPersona()

    listaPersonas.Create("Pepe","Soler","pepe@correo.es")
    listaPersonas.Create("Pablo","Chamorro","pablo@correo.es")
    listaPersonas.Create("rafa","nose","Rafa@correo.es")

    print("Borramos al usuario Pepe con correo: pepe@correo.es")
    listaPersonas.Delete("pepe@correo.es")

    print("Modificamos al usuario 'rafa' por 'Rafa'")
    listaPersonas.Update("rafa@correo.es","Rafa")

    listaPersonas.Mostrar()