import os
import django

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionLibros_Relaciones.settings')
django.setup()

from libros.models import Libro, Editorial, Autor, DatosContacto

# Consultar todos los libros de todas las editoriales

editoriales = Editorial.objects.all()

for editorial in editoriales:
    print(editorial)

    for libro in editorial.libro_set.all():
        print("\t", libro)
