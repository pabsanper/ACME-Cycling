"""ACMECycling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from producto import views
from producto import views as views_pr
from carrito import views as views_ca
from finalizarCompra import views as views_fin
#from django.views.generic.base import TemplateView
#from django.contrib.auth.views import LoginView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_pr.inicio, name='Inicio'),


    path('catalogo/', views_pr.listar, name="Tienda"),

    path('catalogo/producto/<int:id_producto>',views_pr.detalles_productos),
    path("registro/", include("registro.urls")),
    path('productos/producto/<int:id_producto>',views.detalles_productos),

    path('pagos/',views.pago, name='Pago'),
    path('cargo/',views.cargo, name='Cargo'),
    path('productos/producto/<int:id_producto>',views_pr.detalles_productos),

    path('carrito/', views_ca.carrito, name="Carrito"),
    path('agregar/<int:producto_id>/', views_ca.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views_ca.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views_ca.restar_producto, name="Sub"),
    path('limpiar/', views_ca.limpiar_carrito, name="CLS"),
    path('create', views_fin.datos_pago, name='Pagar'),

#    path('cesta/', views_ca.carrito_detail)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)