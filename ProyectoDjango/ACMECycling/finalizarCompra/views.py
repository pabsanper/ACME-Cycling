from decimal import Decimal
import stripe
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from finalizarCompra.models import Venta
from carrito.carrito import Carrito
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.conf import settings
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.template.loader import get_template

def enviar_correo(mail, id, venta):
    mensaje = 'Su pedido ha sido enviado, tiene el siguiente numero de seguimiento: '+id+ ' y ha costado ' + str(venta.precio)+ ' €'
    correo = mail
    context = {'mensaje': mensaje, 'mail': correo}
    plantilla = get_template('plantilla_mail.html')
    content = plantilla.render(context)
    asunto = 'Confirmación del pedido'
    email = EmailMultiAlternatives(asunto, content, settings.EMAIL_HOST_USER, [correo])
    email.fail_silently = False
    email.attach_alternative(content, 'text/html')
    email.send()

def datos_pago(request):
    return render(request, 'pedidos/creaPago.html')

def datos_pago_procesados(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        metodo_pago = request.POST["metodoPago"]
        metodo_envio = request.POST["metodoEnvio"]
        cliente=request.user
        if (metodo_pago=="CR"):
            carrito = Carrito(request)
            precio = carrito.get_total_price()
            if (metodo_envio=="CO"):
                suma=Decimal(2.00)
            else:
                suma=Decimal(00.99)
            
            precio=precio+suma
            
            venta = Venta(nombre=nombre,email=email,dir=direccion,metodoPago=metodo_pago,precio=precio,cliente=cliente,metodoEnvio=metodo_envio)
            venta.save()
            enviar_correo(email, str(venta.id), venta)
            return redirect('Confirmado', str(venta.id))
        if (metodo_pago=="TJ"):
            carrito = Carrito(request)
            precio = carrito.get_total_price()
            if (metodo_envio=="CO"):
                suma=Decimal(2.00)
            else:
                suma=Decimal(0.99)
            
            precio=precio+suma
            
            venta = Venta(nombre=nombre,email=email,dir=direccion,metodoPago=metodo_pago,precio=precio,cliente=cliente,metodoEnvio=metodo_envio)
            venta.save()
            return redirect('/pagos/'+str(venta.id))
            
def pago(request, venta_id):
    venta = Venta.objects.get(id=venta_id)
    return render(request,'pago.html', {'venta': venta})

def cargo(request, venta_id):
    venta = Venta.objects.get(id=venta_id)
    if request.method == 'POST':
        nombre = venta.nombre
        email = venta.email
        customer = stripe.Customer.create(
            email=email,
            name=nombre,
            source = request.POST['stripeToken']
        )

        venta.pagado=True
        venta.save()
        enviar_correo(email, str(venta.id), venta)
        return redirect('Confirmado', str(venta.id))

def pedido_confirmado(request, venta_id): 
    venta = Venta.objects.get(id=venta_id)  
    return render(request,'pedidos/confirmado.html', {'venta': venta}) 

def seguimiento(request):
    id_segui = request.GET.get('searchbarPedido')
    if id_segui:
        venta = Venta.getVentaPorId(id_segui).get()

        return render(request, 'pedidos/seguimientos.html', {'venta': venta})
    else:
        return render(request, 'pedidos/seguimientos.html')
    
