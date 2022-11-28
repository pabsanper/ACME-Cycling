from django.db import models

from django.contrib.auth.models import User



class Venta(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    dir = models.CharField(max_length=250, blank=True)
    creacion = models.DateTimeField(auto_now_add=True, null=True)

    pagado = models.BooleanField(default=False)
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

    class formasEstado(models.TextChoices):
        TRANSITO = 'Transito', 
        PENDIENTE = 'Pendiente'
        ENVIADO = 'Enviado',
        RECIBIDO ='Recibido'

    estado = models.CharField(
        max_length=100,
        choices=formasEstado.choices, default=formasEstado.PENDIENTE,
    )
    

    class Meta:
        ordering = ('-creacion',)

    def __str__(self):
        return 'Venta {}'.format(self.id)
