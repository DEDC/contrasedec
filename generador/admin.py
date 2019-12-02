from django.contrib import admin
from .models import Direcciones, Contrasenas

class DireccionesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'prefijo')

class ContrasenasAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'direccion', 'contrasena')
    list_filter = ('direccion__nombre',)



admin.site.register(Contrasenas, ContrasenasAdmin)
admin.site.register(Direcciones, DireccionesAdmin)