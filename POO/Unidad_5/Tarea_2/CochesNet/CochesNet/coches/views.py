from django.shortcuts import render
from coches.models import Coche, Marca

# Create your views here.
def index(request):
    return render(request,"index.html")

def marcas(request):
    
    marcas = Marca.objects.all()
    
    datos = {
        "marcas": marcas
    }

    return render(request,"marcas.html", datos)

def marca_por_id(request, id):
    marca = Marca.objects.get(pk=id)
    
    datos = {
        "marca": marca
    }

    return render(request,"marca_por_id.html", datos)


def coches(request):
    
    coches = Coche.objects.all().order_by("marca")
    

    datos = {
        "coches": coches
    }

    return render(request,"coches.html", datos)
