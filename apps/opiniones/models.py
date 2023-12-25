from django.db import models
from apps.usuarios.models import Usuarios
from apps.noticias.models import Noticias
import django.utils.timezone
# Create your models here.

class Opinion(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.texto
    class META:
        ordering = ['-fecha']