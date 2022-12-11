from django.db import models
from producto.models import Producto

from django.contrib.auth.models import User



class Venta(models.Model):

    TRANSITO = 'Transito'
    PENDIENTE = 'Pendiente'
    ENVIADO = 'Enviado'
    RECIBIDO ='Recibido'

    CHOICES = ((TRANSITO, TRANSITO),
               (PENDIENTE, PENDIENTE),
               (ENVIADO, ENVIADO),
               (RECIBIDO, RECIBIDO))

    
    nombre = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    dir = models.CharField(max_length=250, blank=True)
    creacion = models.DateTimeField(auto_now_add=True, null=True)

    pagado = models.BooleanField(default=False)
    estado = models.CharField(choices=CHOICES, max_length=1200, default=PENDIENTE)
    class formas_pago(models.TextChoices):
        CONTRAREEMBOLSO = 'CR', 
        TARJETA = 'TJ',

    metodoPago = models.CharField(
        max_length=2,
        choices=formas_pago.choices, default=formas_pago.CONTRAREEMBOLSO,
    )
    class formas_envio(models.TextChoices):
        CORREO = 'CO', 
        SEUR = 'SE',

    metodoEnvio = models.CharField(
        max_length=2,
        choices=formas_envio.choices, default=formas_envio.CORREO,
    )
    precio=models.DecimalField(max_digits=6, decimal_places=2, null=True)

    @staticmethod
    def getVentaPorId(id_venta):
        return Venta.objects.filter(id=id_venta)

    @staticmethod
    def getCantidadVenta(id_venta):
        return cantidad_venta.objects.filter(venta=id_venta)

    class Meta:
        ordering = ('-creacion',)

    def __str__(self):
        return 'Venta {}'.format(self.id)

class cantidad_venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
