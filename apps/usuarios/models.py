from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuarios(AbstractUser):
    nombre = models.CharField(max_length=20)
    apellido =  models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(default="2000-1-1")
    es_colaborador = models.BooleanField(default=False)
    imagen = models.ImageField(null = True, blank = True, upload_to= "usuarios", default="usuarios/default.png")

    def __str__(self):
        return self.nombre