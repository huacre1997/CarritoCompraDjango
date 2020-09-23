from django.template import Library
from ..models import Producto,Plataforma
from django.shortcuts import render, HttpResponse

register=Library()
def filtrarPLataforma(NombPlataforma):
    context=Producto.objects.all().filter(PlatId=NombPlataforma)
    return render( "Views/Default/base.html", context)
register.filter("filtrar",filtrarPLataforma)