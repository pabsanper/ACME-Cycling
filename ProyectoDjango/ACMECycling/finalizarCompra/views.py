from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .forms import VentaCreateForm
from carrito.carrito import Carrito

def datos_pago(request):
    if request.method == 'POST':
        form = VentaCreateForm(request.POST)
        if form.is_valid():
            venta = form.save()
            
            return render(request, 'pedidos/created.html', {'order': venta})
    else:
        form = VentaCreateForm()

    return render(request, 'pedidos/creaPago.html', {'form': form})
