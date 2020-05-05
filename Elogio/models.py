from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Elogio(models.Model):
    nome = models.CharField(default='AA', max_length=250, verbose_name='Nome')
    comentario = models.TextField(verbose_name='Comentario')
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_comentario = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_comentario
