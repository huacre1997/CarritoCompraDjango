from django.shortcuts import render, HttpResponse
from ..models import Producto,Plataforma,Genero

class ProductsController:
     def index(self,PlatId):
       
       
        CatalProducts = Producto.objects.filter(PlatId=PlatId)        
      

        context = {"CatalProducts":CatalProducts}
        return render(self, "Views/Index/ListView.html", context)
