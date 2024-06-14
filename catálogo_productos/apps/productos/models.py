from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey('Categoria', related_name='productos', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    # imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



