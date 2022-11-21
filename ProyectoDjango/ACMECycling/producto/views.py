from producto.models import Producto, Categoria
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.conf import settings
from django.db.models import Q

#muestra los títulos de las recetas que están registradas
def inicio(request):
    productos=Producto.objects.all()
    return render(request,'inicio.html', {'productos':productos})

def detalles_productos(request, id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    return render(request, 'productos/detalles.html', {'producto': producto})
    
def buscador(request):
    busqueda = request.GET.get("buscar")
    productos = Producto.objects.all()

    if busqueda:
        productos = Producto.objects.filter( Q(nombre__icontains = busqueda) |
                                             Q(descripcion__icontains = busqueda) |
                                             Q(categoria__icontains = busqueda)).distinct()
    
    return render(request, 'catalogo.html', {'productos':productos})

def listar(request):
    return render(request, 'catalogo.html', {'productos': Producto.objects.all()})
