import os
import django

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionLibros.settings')
django.setup()

from libros.models import Libro

    

class Main():
    @staticmethod
    def main():
        os.system("clear")
        libros = Libro.objects.all()
        
        for l in libros:
            print(l.__str__())
        
if __name__=="__main__":
    Main.main()