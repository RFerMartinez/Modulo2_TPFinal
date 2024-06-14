from django.db import models

from ..usuarios.models import Usuario

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

# Tabla inermedia en una relación N:N entre Usuario -- tieneFav -- Producto
class Favorito(models.Model):
    producto = models.ForeignKey(Producto, related_name='favoritos', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name='usuario_fav', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} - {self.producto.nombre}'




