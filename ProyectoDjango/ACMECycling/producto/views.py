from producto.models import Producto, Categoria
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.conf import settings
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.template.loader import get_template

#muestra los títulos de las recetas que están registradas
def enviar_correo(mail):
    mensaje = 'Su pedido ha sido enviado'
    correo = mail
    context = {'mensaje': mensaje, 'mail': correo}
    plantilla = get_template('plantilla_mail.html')
    content = plantilla.render(context)
    asunto = 'Confirmación del pedido'
    email = EmailMultiAlternatives(asunto, content, settings.EMAIL_HOST_USER, [correo])
    email.fail_silently = False
    email.attach_alternative(content, 'text/html')
    email.send()

def inicio(request):
    productos=Producto.objects.all()
    return render(request,'inicio.html', {'productos':productos})

def detalles_productos(request, id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    if (request.method=='POST'):
        enviar_correo('pablitosantospsp@gmail.com')

    return render(request, 'productos/detalles.html', {'producto': producto})
    

def listar(request):
    busqueda = request.GET.get("buscar")
    print(busqueda)
    if busqueda:
        pr_name = Producto.objects.filter(nombre__icontains = busqueda)
        pr_descripcion = Producto.objects.filter(descripcion__icontains = busqueda)
        pr_categoria = Producto.objects.filter(categoria__icontains = busqueda)
        pr_fabricante = Producto.objects.filter(fabricante__icontains = busqueda)
        p = (pr_name | pr_descripcion | pr_categoria | pr_fabricante)
    else:
        p = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos':p})

