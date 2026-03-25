import os
import django

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionLibros_Relaciones.settings')
django.setup()

from libros.models import Libro, Editorial, Autor, DatosContacto

# Realiza un listado de los autores y sus libros

autores = Autor.objects.all()

for autor in autores:
    print(f"{autor.nombre}:")

    for libro in autor.libros.all():
        print(f"\t{libro}")

