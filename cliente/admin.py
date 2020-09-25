from django.contrib import admin

from django.contrib.auth import get_user_model
from .models import *
admin.site.register(get_user_model())
class DomicilioAdmin(admin.ModelAdmin):
    list_display  = ('cliente',"direccion","referencia","distrito","provincia","departamento")
admin.site.register(Domicilio, DomicilioAdmin)
