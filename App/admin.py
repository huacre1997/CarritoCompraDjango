from django.contrib import admin

from .models import Producto, Genero, Plataforma
from django.utils.html import format_html


class PlataformAdmin(admin.ModelAdmin):
    list_display = ("PlatName", "PlatEsta")


class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("GenNomb", "GenEsta")


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("ProdName", "ProdCost", "GeneroName",
                    "PlatId", "ProdStock", "ProdEstado")
 

    def GeneroName(self, obj):
        return "/".join([c.GenNomb for c in obj.GenId.all().order_by("GenNomb")])
    search_fields = ("ProdClasi", "ProdCost", "PlatId")
    list_filter = ("ProdClasi", "PlatId__PlatName", "GenId__GenNomb","ProdMarca")


    def image_tag(self, obj):
        if obj.ProdImg != None:
            return format_html("<img width='85' height='100' src='/media/{}'/>".format(obj.ProdImg))

       

    readonly_fields = ["image_tag","created","updated"]


admin.site.register(Plataforma, PlataformAdmin)
admin.site.register(Genero, CategoriasAdmin)
admin.site.register(Producto, ProductoAdmin)
