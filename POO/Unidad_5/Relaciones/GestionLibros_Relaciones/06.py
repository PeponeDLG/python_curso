import os
import django

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionLibros_Relaciones.settings')
django.setup()

from libros.models import Libro, Editorial, Autor, DatosContacto

# Realiza un listado de los libros y sus autores correspondientes

libros = Libro.objects.all()

for libro in libros:
    print(f"Autor \"{libro}\":")

    for autor in libro.autor_set.all():
        print(f"\t{autor.nombre}")
