from django.db import models
from django.utils.timezone import now


class Plataforma(models.Model):
    PlatId = models.AutoField(primary_key=True)
    PlatName = models.CharField(max_length=50, verbose_name="Plataforma")
    PlatEsta = models.BooleanField(verbose_name="Estado", default=True)
    
    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"
        ordering = ["PlatName"]
    def __str__(self):
        return self.PlatName
class Genero(models.Model):
    GenId = models.AutoField(primary_key=True)
    GenNomb = models.CharField(max_length=50)
    GenEsta = models.BooleanField(verbose_name="Estado", default=True)
    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ["GenNomb"]
    def __str__(self):
        return self.GenNomb
    

class Producto(models.Model):
    clasi = [("TODAS LAS EDADES", "TODOS"), ("MAYORES DE 10 AÑOS", "TODOS+10"), ("MAYORES DE 13 AÑOS", "ADOLESCENTES"),
             ("MAYORES DE 17 AÑOS", "MATURE+17"), ("MAYORES DE 18 AÑOS", "MATURE+18"), ("SIN CLASIFICAR", "SIN CLASIFICAR")]
    ProductoId = models.AutoField(primary_key=True)
    ProdName = models.CharField(max_length=50, verbose_name="Título")
    ProdDesc = models.TextField(max_length=1000, verbose_name="Descripción")
    ProdCost = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True,verbose_name="Costo")
    ProdStock = models.SmallIntegerField(default=0, verbose_name="Stock")
    GenId = models.ManyToManyField(Genero,verbose_name="Género")
    ProdMarca=models.CharField(max_length=50, verbose_name="Marca",default="")
    ProdClasi = models.CharField(
        verbose_name="Clasificación ESRB", choices=clasi, max_length=20)
    PlatId = models.ForeignKey(Plataforma, verbose_name="Plataforma",on_delete=models.CASCADE,null=True)

    ProdImg = models.ImageField(
        null=True, upload_to="image/curso", verbose_name="Imagen")
    ProdPrev = models.BooleanField(verbose_name="Preventa", default=False)
    ProdEstado = models.BooleanField(verbose_name="Estado", default=True)
    ProdFechaLan=models.DateField(verbose_name="Fecha de lanzamiento",null=True,blank=True)
    PreFinalPrev= models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True,verbose_name="Precio final preventa")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")
    class Meta:
        verbose_name = "Videojuego"
        verbose_name_plural = "Videojuegos"
        ordering = ["created"]
        get_latest_by="created"

    def __str__(self):
        return self.ProdName
   