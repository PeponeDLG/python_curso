import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CochesNet.settings")
django.setup()

from coches.models import Marca, Coche

print("Creando marcas...")

marcas = [
    Marca(nombre="Audi", pais="Alemania"),
    Marca(nombre="Ford", pais="Estados Unidos"),
    Marca(nombre="Renault", pais="Francia"),
    Marca(nombre="Seat", pais="España"),
    Marca(nombre="Fiat", pais="Italia"),
    Marca(nombre="Toyota", pais="Japón"),
    Marca(nombre="Hyundai", pais="Corea del Sur"),
    Marca(nombre="Volvo", pais="Suecia"),
    Marca(nombre="Volkswagen", pais="Alemania"),
    Marca(nombre="Peugeot", pais="Francia"),
    Marca(nombre="BMW", pais="Alemania"),
    Marca(nombre="Mercedes", pais="Alemania"),
    Marca(nombre="Honda", pais="Japón"),
    Marca(nombre="Nissan", pais="Japón"),
]
for marca in marcas:
    marca.save()

coches = [
    Coche(marca=Marca.objects.get(nombre="Audi"), modelo="A3", precio=30000, potencia=150, color="Blanco", fecha_fabricacion="2021-01-01"),
    Coche(marca=Marca.objects.get(nombre="Ford"), modelo="Focus", precio=25000, potencia=120, color="Negro", fecha_fabricacion="2021-01-01"),
    Coche(marca=Marca.objects.get(nombre="Audi"), modelo="A4", precio=35000, potencia=200, color="Gris", fecha_fabricacion="2022-10-10"),
    Coche(marca=Marca.objects.get(nombre="Audi"), modelo="A3", precio=30000, potencia=150, color="Blanco", fecha_fabricacion="2021-01-01"),
    Coche(marca=Marca.objects.get(nombre="Ford"), modelo="Focus", precio=25000, potencia=120, color="Negro", fecha_fabricacion="2021-01-01"),
    Coche(marca=Marca.objects.get(nombre="Audi"), modelo="A4", precio=35000, potencia=200, color="Gris", fecha_fabricacion="2022-10-20"),
    Coche(marca=Marca.objects.get(nombre="Peugeot"), modelo="208", precio=20000, potencia=100, color="Rojo", fecha_fabricacion="2020-05-15"),
    Coche(marca=Marca.objects.get(nombre="Peugeot"), modelo="308", precio=22000, potencia=130, color="Azul", fecha_fabricacion="2019-03-10"),
    Coche(marca=Marca.objects.get(nombre="Ford"), modelo="Mustang", precio=45000, potencia=300, color="Amarillo", fecha_fabricacion="2021-07-07"),
    Coche(marca=Marca.objects.get(nombre="Audi"), modelo="A3", precio=30000, potencia=150, color="Blanco", fecha_fabricacion="2021-01-01"),
    Coche(marca=Marca.objects.get(nombre="Ford"), modelo="Focus", precio=25000, potencia=120, color="Negro", fecha_fabricacion="2021-01-01"),
    Coche(marca=Marca.objects.get(nombre="Audi"), modelo="A4", precio=35000, potencia=200, color="Gris", fecha_fabricacion="2022-10-20"),
    Coche(marca=Marca.objects.get(nombre="Peugeot"), modelo="208", precio=20000, potencia=100, color="Rojo", fecha_fabricacion="2020-05-15"),
    Coche(marca=Marca.objects.get(nombre="Peugeot"), modelo="308", precio=22000, potencia=130, color="Azul", fecha_fabricacion="2019-03-10"),
    Coche(marca=Marca.objects.get(nombre="Ford"), modelo="Mustang", precio=45000, potencia=300, color="Amarillo", fecha_fabricacion="2021-07-07"),
    Coche(marca=Marca.objects.get(nombre="BMW"), modelo="X5", precio=60000, potencia=250, color="Negro", fecha_fabricacion="2021-09-15"),
    Coche(marca=Marca.objects.get(nombre="BMW"), modelo="X3", precio=50000, potencia=200, color="Blanco", fecha_fabricacion="2020-11-20"),
    Coche(marca=Marca.objects.get(nombre="Mercedes"), modelo="C-Class", precio=55000, potencia=220, color="Gris", fecha_fabricacion="2021-03-25"),
    Coche(marca=Marca.objects.get(nombre="Mercedes"), modelo="E-Class", precio=70000, potencia=300, color="Azul", fecha_fabricacion="2022-01-10"),
    Coche(marca=Marca.objects.get(nombre="Toyota"), modelo="Corolla", precio=20000, potencia=120, color="Rojo", fecha_fabricacion="2020-06-30"),
    Coche(marca=Marca.objects.get(nombre="Toyota"), modelo="Camry", precio=25000, potencia=150, color="Blanco", fecha_fabricacion="2021-02-14"),
    Coche(marca=Marca.objects.get(nombre="Honda"), modelo="Civic", precio=22000, potencia=140, color="Negro", fecha_fabricacion="2020-08-05"),
    Coche(marca=Marca.objects.get(nombre="Honda"), modelo="Accord", precio=28000, potencia=180, color="Gris", fecha_fabricacion="2021-04-18"),
    Coche(marca=Marca.objects.get(nombre="Nissan"), modelo="Altima", precio=24000, potencia=160, color="Azul", fecha_fabricacion="2020-12-12"),
    Coche(marca=Marca.objects.get(nombre="Nissan"), modelo="Maxima", precio=30000, potencia=200, color="Blanco", fecha_fabricacion="2021-05-22"),
]

print("Creando Coches")
for coche in coches:
    coche.save()    
    
