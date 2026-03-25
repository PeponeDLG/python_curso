import os
import django

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionLibros_Relaciones.settings')
django.setup()

from libros.models import Libro, Editorial, Autor, DatosContacto

# Consulta todos los autores y sus datos de contacto

autores = Autor.objects.all()

for autor in autores:
    print(f"\n\t - {autor.nombre} - {autor.pais}")

