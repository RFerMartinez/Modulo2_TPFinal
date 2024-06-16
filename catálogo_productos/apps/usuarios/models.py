from django.contrib.auth.models import AbstractUser

from django.db import models

class Usuario(AbstractUser):
    
    # Se le agrega los campos booleanos -> es_admin
    es_admin = models.BooleanField(default=False)
    imagen = models.ImageField(null=True, blank=True, upload_to="imagenPerfil/")

    # Redefinir el método 'str'
    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.username})"


