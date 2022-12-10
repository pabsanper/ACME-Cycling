from django.contrib import admin
from django.urls import path,include
from producto import views as views_pr
from carrito import views as views_ca

from finalizarCompra import views as views_fin
from fqs import views as views_fqs


from registro import views as views_reg

from django.contrib.auth.views import LoginView,LogoutView


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_pr.inicio, name='Inicio'),


    path('fqs/', views_fqs.inicio, name="Preguntas"),

    path('catalogo/', views_pr.listar, name="Tienda"),

    path('fabricantes/', views_pr.listar_fabricantes, name="Fabricantes"),
    path('fabricantes/<int:id_fabricante>/', views_pr.listar_productos_fabricante),

    path('categorias/', views_pr.listar_categorias, name="Categorias"),
    path('categorias/<int:id_categoria>/', views_pr.listar_productos_categoria),

    path('catalogo/producto/<int:id_producto>',views_pr.detalles_productos, name='Detalles'),
    path('pagos/<int:venta_id>',views_fin.pago, name='Pago'),
    path('cargo/<int:venta_id>',views_fin.cargo, name='Cargo'),
    path('pedidoConfirmado/<int:venta_id>',views_fin.pedido_confirmado, name='Confirmado'),
    path('registro/login/',LoginView.as_view(),name="login_url"),
    path('registro/registro',views_reg.register_view,name="register_url"),
    path('registro/logout/',LogoutView.as_view(),name="logout"),

    path('carrito/', views_ca.carrito, name="Carrito"),
    path('agregar/<int:producto_id>/', views_ca.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views_ca.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views_ca.restar_producto, name="Sub"),
    path('limpiar/', views_ca.limpiar_carrito, name="CLS"),
    path('create/', views_fin.datos_pago, name='Pagar'),
    path('procesarPagos/',views_fin.datos_pago_procesados, name='Procesar'),

    path('seguimiento/', views_fin.seguimiento, name='seguimiento'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)