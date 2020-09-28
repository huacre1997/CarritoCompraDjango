from django.shortcuts import render, HttpResponse
from ..models import Producto,Plataforma,Genero


class IndexController():

    def index(request):
        CarrProducts = Producto.objects.all().order_by("created")[:10][::-1]
        CatalProducts=Producto.objects.all()
        Plataformas = Plataforma.objects.all()
        Clasi=Producto.clasi
        Clasificacion=[ ]
        for x in range(0,len(Clasi)):
            Clasificacion.append(Clasi[x][0])

        Generos=Genero.objects.all()

        context = {"CarrProducts": CarrProducts,"CatalProducts":CatalProducts,"Plataforma":Plataformas,"Genero":Generos,"Clasi":Clasificacion}
        return render(request, "Default/base.html", context)
    def List(request):
        Productos = Producto.objects.all()
        Plataformas = Plataforma.objects.all()
        Clasi=Producto.clasi
        Clasificacion=[ ]
        for x in range(0,len(Clasi)):
            Clasificacion.append(Clasi[x][0])
        Generos=Genero.objects.all()

        context = {"Productos": Productos,"Plataforma":Plataformas,"Genero":Generos,"Clasi":Clasificacion}
        return render(request, "Default/ListView.html", context)
    def about(request):
        return render(request, "Index/index.html")
    def details(request,idproducto):
        Productos = Producto.objects.get(ProductoId=idproducto)
        context = {"details": Productos}
        return render(request, "Index/details.html", context)
    def filtrar(self,PlatId):
        print(PlatId) 

        if PlatId!=0:
            CatalProducts = Producto.objects.filter(PlatId=PlatId)        
        else:
            CatalProducts = Producto.objects.all()      


        context = {"CatalProducts":CatalProducts}
        return render(self, "Index/ListView.html", context)


