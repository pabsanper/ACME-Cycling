from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Fabricante(models.Model):
    nombre = models.CharField(max_length=100)
    #primerApellido = models.CharField(max_length=100)
    #segundoApellido = models.CharField(max_length=100)
    #pais = models.CharField(max_length=50)
    #edad = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default='1')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, default='2')
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, default='3')
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to= 'productos/', verbose_name='Imagen', default='productos/noimage.jpg')
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

