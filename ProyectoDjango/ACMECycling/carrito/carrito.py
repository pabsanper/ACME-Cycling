from decimal import Decimal
from django.conf import settings

class Carrito(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        c = self.session.get("carrito")
        if not c:
            self.session["carrito"] = {}
            self.c = c
        else:
            self.c= c

    def agregar(self, producto):
        id_carrito = str(producto.id)
        if id_carrito not in self.c.keys():
            self.c[id_carrito] = {
                "producto_id" : producto.id,
                "nombre" : producto.nombre,
                "precio" : float(producto.precio),
                "cantidad" : int(1),
            }
        else:
            self.c[id]["cantidad"] += 1
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"]  = self.c
        self.session.modified = True

    def eliminar(self, producto):
        id_carrito = str(producto.id)
        if id_carrito in self.c:
            del self.c[id_carrito]
            self.guardar_carrito()

    def restar(self, producto):
        id_carrito = str(producto.id)
        if id_carrito in self.c.keys():
            self.c[id_carrito]["cantidad"] -= 1
            if self.c[id_carrito]["cantidad"] <= 0 :
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.c.values())

    def get_items(self):
        return self.c.values()