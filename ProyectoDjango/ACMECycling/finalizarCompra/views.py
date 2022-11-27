from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import OrderItem, Order
from .forms import OrderCreateForm
from carrito.carrito import Carrito

def order_create(request):
    cart = Carrito(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, productoId=item['producto_id'],nombre=item['nombre'], precio=item['precio'], cantidad=item['cantidad'])
            cart.clear()
            #send mail
            
            return render(request, 'pedidos/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'pedidos/create.html', {'cart': cart, 'form': form})

#@staff_member_required
#def admin_order_detail(request, order_id):
 #   order = get_object_or_404(Order, id=order_id)
 #   return render(request, 'admin/orders/order/detail.html', {'order': order})