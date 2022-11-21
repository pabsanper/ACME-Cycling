from django.shortcuts import render
from django.db.models import Q
from producto.models import Producto

# Create your views here.
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

