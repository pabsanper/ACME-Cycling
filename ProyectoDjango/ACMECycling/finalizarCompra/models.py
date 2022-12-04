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
    class formasPago(models.TextChoices):
        CONTRAREEMBOLSO = 'CR', 
        TARJETA = 'TJ',

    metodoPago = models.CharField(
        max_length=2,
        choices=formasPago.choices, default=formasPago.CONTRAREEMBOLSO,
    )
    class formasEnvio(models.TextChoices):
        CORREO = 'CO', 
        SEUR = 'SE',

    metodoEnvio = models.CharField(
        max_length=2,
        choices=formasEnvio.choices, default=formasEnvio.CORREO,
    )
    precio=models.DecimalField(max_digits=6, decimal_places=2, null=True)

    # class formasEstado(models.TextChoices):
    #     TRANSITO = 'Transito', 
    #     PENDIENTE = 'Pendiente'
    #     ENVIADO = 'Enviado',
    #     RECIBIDO ='Recibido'

    # estado = models.CharField(
    #     max_length=100,
    #     choices=formasEstado.choices, default=formasEstado.PENDIENTE,
    # )

    @staticmethod
    def getVentaPorId(ventaID):
        return Venta.objects.filter(id=ventaID)

    @staticmethod
    def getCantidadVenta(ventaID):
        return cantidadVenta.objects.filter(venta=ventaID)

    class Meta:
        ordering = ('-creacion',)

    def __str__(self):
        return 'Venta {}'.format(self.id)


#===========================================================

# class Seguimiento(models.Model):
#         seguimiento_id = models.CharField(max_length=70)
#         estado = models.ForeignKey(Venta, on_delete=models.CASCADE)

class cantidadVenta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
