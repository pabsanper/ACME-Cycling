from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from producto.models import Producto
from django.contrib.auth.models import User
import django.db.models.deletion


class Venta(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    dirreccion = models.CharField(max_length=250)
    creacion = models.DateTimeField(auto_now_add=True)

    pagado = models.BooleanField(default=False)
    class formasPago(models.TextChoices):
        CONTRAREEMBOLSO = 'CR', 
        TARJETA = 'TJ',

    metodoPago = models.CharField(
        max_length=2,
        choices=formasPago.choices,
    )

    class Meta:
        ordering = ('-creacion',)

    def __str__(self):
        return 'Venta {}'.format(self.id)

