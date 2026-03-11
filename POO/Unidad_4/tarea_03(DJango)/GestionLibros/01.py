import os
import django

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionLibros.settings')
django.setup()

from libros.models import Libro

# insertamos algunos libros en el modelo Libro

libros = [
    Libro(titulo="El Señor de los Anillos", autor="J.R.R. Tolkien", precio=19.99, editorial="Editorial A", fecha_lanzamiento="1954-01-01"),
    Libro(titulo="El Hobbit", autor="J.R.R. Tolkien", precio=14.99, editorial="Editorial B", fecha_lanzamiento="1937-01-01"),
    Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", precio=9.99, editorial="Editorial C", fecha_lanzamiento="1967-01-01"),
    Libro(titulo="Don Quijote de la Mancha", autor="Miguel de Cervantes", precio=12.99, editorial="Editorial D", fecha_lanzamiento="1605-01-01"),
    Libro(titulo="El Principito", autor="Antoine de Saint-Exupery", precio=8.99, editorial="Editorial E", fecha_lanzamiento="1943-01-01")
]

for libro in libros:
    print(f"Guardando libro: {libro.titulo}")
    libro.save()