from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from producto.models import Producto
from decimal import Decimal
import django.db.models.deletion


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_subtotal(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=django.db.models.deletion.DO_NOTHING, related_name='items')
    product = models.ForeignKey(Producto,on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
