import os
import django

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionLibros_Relaciones.settings')
django.setup()

from libros.models import Libro, Editorial, Autor, DatosContacto

# insertamos alguna editoriales en el model Editorial
editoriales = [
    Editorial(nombre="Editorial A", pais="España"),
    Editorial(nombre="Editorial B", pais="Francia"),
    Editorial(nombre="Editorial C", pais="Italia"),
    Editorial(nombre="Editorial D", pais="Alemania"),
    Editorial(nombre="Editorial E", pais="Portugal")
]

for editorial in editoriales:
    print(f"Guardando editorial: {editorial.nombre}")
    editorial.save()

# Insertamos algunos libros en el modelo Libro

libros = [
    Libro(titulo="El Señor de los Anillos", precio=19.99, editorial_id=1, fecha_lanzamiento="1954-01-01"),
    Libro(titulo="Cien años de soledad", precio=9.99, editorial_id=2, fecha_lanzamiento="1967-01-01"),
    Libro(titulo="Don Quijote de la Mancha", precio=12.99, editorial_id=3, fecha_lanzamiento="1605-01-01"),
    Libro(titulo="El Principito", precio=8.99, editorial_id=4, fecha_lanzamiento="1943-01-01"),
    Libro(titulo="1984", precio=29.99, editorial_id=5, fecha_lanzamiento="1949-06-08"),
    Libro(titulo="La Divina Comedia", precio=49.99, editorial_id=3, fecha_lanzamiento="1320-01-01"),
    Libro(titulo="Romeo y Julieta", precio=39.99, editorial_id=4, fecha_lanzamiento="1597-01-01"),
    Libro(titulo="El código Da Vinci", precio=19.99, editorial_id=1, fecha_lanzamiento="2003-01-01"),
    Libro(titulo="El diario de Ana Frank", precio=19.99, editorial_id=1, fecha_lanzamiento="1947-06-22"),
    Libro(titulo="Harry Potter y la piedra filosofal", precio=59.99, editorial_id=1, fecha_lanzamiento="1997-06-26")
]

for libro in libros:
    print(f"Guardando libro: {libro.titulo}")
    libro.save()

# Insertamos algunos autores para los libros anteriores
autores = [
    Autor(nombre="J.R.R. Tolkien", pais="Inglaterra"),
    Autor(nombre="Gabriel García Márquez", pais="Colombia"),
    Autor(nombre="Miguel de Cervantes", pais="España"),
    Autor(nombre="Antoine de Saint-Exupery", pais="Francia"),
    Autor(nombre="George Orwell", pais="Inglaterra"),
    Autor(nombre="Dante Alighieri", pais="Italia"),
    Autor(nombre="William Shakespeare", pais="Reino Unido"),
    Autor(nombre="Dan Brown", pais="Estados Unidos"),
    Autor(nombre="Ana Frank", pais="Alemania"),
    Autor(nombre="J.K. Rowling", pais="Reino Unido")
]

for autor in autores:
    print(f"Guardando autor: {autor.nombre}")
    autor.save()

## Asignamos los autores a los libros, para ello tenemos que recorrer los libros y asignarle el autor correspondiente

autores = Autor.objects.all()
libros = Libro.objects.all()

i = 0
for autor in autores: # Recorremos los autores
    libro = libros[i] # Asignamos el libro correspondiente en orden de inserción de los libros
    autor.libros.add(libro) # Asignamos el libro al autor
    autor.save() # Guardamos el autor con el libro correspondiente
    print(f"Libro '{libro.titulo}' asignado al autor '{autor.nombre}'")
    i += 1


# Insertamos algunos datos de contacto para los autores
datos_contacto = [
    DatosContacto(email="j6B9W@example.com", telefono="123456789", autor_id=1),
    DatosContacto(email="t9oEa@example.com", telefono="987654321", autor_id=2),
    DatosContacto(email="BbHbA@example.com", telefono="555555555", autor_id=3),
    DatosContacto(email="vDm0d@example.com", telefono="111111111", autor_id=4),
    DatosContacto(email="fUk0t@example.com", telefono="222222222", autor_id=5),
    DatosContacto(email="0tIu0@example.com", telefono="333333333", autor_id=6),
    DatosContacto(email="V6PwR@example.com", telefono="444444444", autor_id=7),
    DatosContacto(email="GZBdD@example.com", telefono="555555555", autor_id=8),    
    DatosContacto(email="hXr0l@example.com", telefono="666666666", autor_id=9),
    DatosContacto(email="GZBdD@example.com", telefono="777777777", autor_id=10)
]

for contacto in datos_contacto:
    print(f"Guardando contacto: {contacto.email}")
    contacto.save()