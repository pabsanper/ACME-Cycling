from decimal import Decimal
from django.conf import settings
from .models import *
#from producto.models import Producto

class Carrito(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = carrito
        else:
            self.carrito= carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id" : producto.id,
                "nombre" : producto.nombre,
                "precio" : float(producto.precio),
                "cantidad" : int(1),
            }
        else:
            self.carrito[id]["cantidad"] += 1
            #self.carrito[id]["acumulado"] += float(producto.precio)
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"]  = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            #self.carrito[id]["acumulado"] -= float(producto.precio)
            if self.carrito[id]["cantidad"] <= 0 :
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carrito.values())

    def get_items(self):
        return self.carrito.values()