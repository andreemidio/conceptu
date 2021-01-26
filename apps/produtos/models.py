import uuid

from django.db import models

# Create your models here.
from apps.categorias.models import Categorias
from apps.usuarios.models import Usuarios


class Produtos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Categorias)
    criado_por = models.ForeignKey(
        Usuarios, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='produtos_criado_por_usuarios')

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-data_criacao']
