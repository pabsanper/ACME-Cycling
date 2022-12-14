
import stripe

from producto.models import Producto, Categoria, Fabricante

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.db.models import Q
from django.views import View
from django.http import JsonResponse
    
def inicio(request):
    productos=Producto.objects.all()
    return render(request,'inicio.html', {'productos':productos})

def detalles_productos(request, id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    return render(request, 'productos/detalles.html', {'producto': producto})
    

def listar(request):
    busqueda = request.GET.get("buscar")
    print(busqueda)
    if busqueda:
        pr_name = Producto.objects.filter(nombre__icontains = busqueda)
        pr_descripcion = Producto.objects.filter(descripcion__icontains = busqueda)
        pr_categoria = Producto.objects.filter(categoria__nombre__icontains = busqueda)
        pr_fabricante = Producto.objects.filter(fabricante__nombre__icontains = busqueda)
        p = (pr_name | pr_descripcion | pr_categoria | pr_fabricante)
    else:
        p = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos':p})


def listar_fabricantes(request):
    fabricantes = Fabricante.objects.all()
    return render(request, 'listadoFabricantes.html', {'fabricantes': fabricantes})

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'listadoCategorias.html', {'categorias': categorias})

def listar_productos_fabricante(request, id_fabricante):
    fabricante = get_object_or_404(Fabricante, id=id_fabricante)
    productos = Producto.objects.filter(fabricante__nombre__icontains = fabricante)
    return render(request, 'catalogo.html', {'productos': productos})

def listar_productos_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id=id_categoria)
    productos = Producto.objects.filter(categoria__nombre__icontains = categoria)
    return render(request, 'catalogo.html', {'productos': productos})
