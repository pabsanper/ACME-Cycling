from producto.models import Producto, Categoria
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.conf import settings

#muestra los títulos de las recetas que están registradas
def inicio(request):
    productos=Producto.objects.all()
    return render(request,'inicio.html', {'productos':productos})

def detalles_productos(request, id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    return render(request, 'productos/detalles.html', {'producto': producto})