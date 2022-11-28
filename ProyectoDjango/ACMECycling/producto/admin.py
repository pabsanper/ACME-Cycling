from django.contrib import admin
from producto.models import Categoria, Producto, Departamento, Fabricante

admin.site.register(Categoria)
admin.site.register(Departamento)
admin.site.register(Fabricante)
admin.site.register(Producto)

