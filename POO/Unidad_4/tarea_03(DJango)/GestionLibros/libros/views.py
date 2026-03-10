from django.shortcuts import render
from django.http import HttpResponse
from libros.models import Libro

# Create your views here.
def index(request):
    return HttpResponse("Indice de Gestión de Libros.")

def listado(request):
    return HttpResponse("<h1>Listado de libros</h1>")

def saludo(request):
    datos = {
        "mensajes": "Hola Mundo",
        "fecha": "09-09-2025",
        "lista": [10,20,30,40,50]
    }
    return render(request,"saludo.html",context=datos)

def listado_libros(request):
    libros = Libro.objects.all()
    return render(request, "listado_libros.html", {"libros": libros})