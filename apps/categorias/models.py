import uuid

from django.db import models

# Create your models here.
from apps.usuarios.models import Usuarios


class Categorias(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_categoria = models.CharField(max_length=255, unique=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(
        Usuarios, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='categorias_criado_por_usuarios')

    def __str__(self):
        return self.nome_categoria

    def __repr__(self):
        return self.nome_categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-data_criacao']

