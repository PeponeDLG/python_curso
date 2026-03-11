import os
import django

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CursosFormacion.settings')
django.setup()

from curso.models import Curso

# insertamos algunos libros en el modelo Libro

curso = [
    # Curso(nombre="curso1", descripcion="curso 1", horas="1", tipo="tipo 1", fecha_inicio="2026-01-01", fecha_fin="2026-02-01", precio="5"),
    # Curso(nombre="curso2", descripcion="curso 2", horas="2", tipo="tipo 2", fecha_inicio="2026-02-01", fecha_fin="2026-03-01", precio="7"),
    # Curso(nombre="curso3", descripcion="curso 3", horas="3", tipo="tipo 3", fecha_inicio="2026-03-01", fecha_fin="2026-04-01", precio="8"),
    # Curso(nombre="curso4", descripcion="curso 4", horas="4", tipo="tipo 4", fecha_inicio="2026-04-01", fecha_fin="2026-05-01", precio="9"),
    Curso(nombre="curso5", descripcion="curso 5", horas="5", tipo="tipo 4", fecha_inicio="2026-04-01", fecha_fin="2026-05-01", precio="9"),
    
]

for c in curso:
    print(f"Guardando curso: {c.nombre}")
    c.save()