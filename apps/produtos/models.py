from django.db import models

# Create your models here.
from apps.categorias.models import Categorias


class Produtos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categorias = models.ManyToManyField(Categorias)
