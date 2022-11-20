from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default='')
    nombre = models.CharField(max_length=200)
    #imagen = models.ImageField(upload_to= 'recetas', verbose_name='Imagen')
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre