from django.shortcuts import render
from coches.models import Coche, Marca
from django.db.models import Count, Avg
import plotly.express as px

# Create your views here.
def index(request):
    return render(request,"index.html")

def lineas(request):
    
    precio_medio_marca = Coche.objects.values_list("fecha_fabricacion__year").annotate(numero=Count("id"))
    marcas = [elemento[0] for elemento in precio_medio_marca]
    fechas = [elemento[1] for elemento in precio_medio_marca]

    fig = px.line(x=marcas, y=fechas, title="Año de abricacion")
    
    grafico = fig.to_html(full_html=False)

    datos = {
        "grafico": grafico
    }

    return render(request,"lineas.html", datos)


def barras(request):
    
    precio_medio_marca = Coche.objects.values_list("marca__nombre").annotate(numero=Avg("id"))
    marcas = [elemento[0] for elemento in precio_medio_marca]
    precios = [elemento[1] for elemento in precio_medio_marca]

    fig = px.bar(x=marcas, y=precios, title="Nº de coches por marca")
    
    grafico = fig.to_html(full_html=False)

    datos = {
        "grafico": grafico
    }

    return render(request,"barras.html", datos)

def sectores(request):
    
    coches_por_marca = Coche.objects.values_list("marca__nombre").annotate(numero=Count("id"))
    marcas = [elemento[0] for elemento in coches_por_marca]
    num_coches = [elemento[1] for elemento in coches_por_marca]

    fig = px.pie(values=num_coches, names=marcas, title="Nº de coches por marca")
    
    grafico = fig.to_html(full_html=False)

    datos = {
        "grafico": grafico
    }

    return render(request,"sectores.html", datos)

def marcas(request):
    
    marcas = Marca.objects.all().order_by("nombre")
    print("\n"*5,"pasa","\n"*5)
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
