# ALUMNO AGUSTIN LUCAS PONCE DE LEON
# PROYECTO PYTHON - CURSO CODER HOUSE

from django.contrib import admin
from .models import *
from datetime import datetime

#TODOS ESTOS ATRIBUTOS ESTAN EN LA DOCUMENTACION DEL ADMIN DE DJANGO
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'marca', 'fecha_creacion', 'talle', 'precio', 'antiguedad']
    search_fields = ['nombre', 'marca']
    list_filter = ['nombre']

    def antiguedad(self, object):
        print('*******',object)
        if object.fecha_creacion:
            return (datetime.now().date() - object.fecha_creacion).days

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Proveedor)
admin.site.register(Avatar)