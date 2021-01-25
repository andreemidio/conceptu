from django.contrib.auth.models import User
from rest_framework import serializers

from apps.categorias.models import Categorias
from apps.usuarios.models import Usuarios
from apps.usuarios.serializers import GetUsuariosSerializers


class PostCategoriaSerializers(serializers.ModelSerializer):
    nome_categoria = serializers.CharField(required=True)
    criado_por = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, queryset=Usuarios.objects.all())

    class Meta:
        model = Categorias
        fields = ('nome_categoria', 'criado_por')


class ListCategoriaSerializers(serializers.ModelSerializer):
    nome_categoria = serializers.CharField(required=True)
    criado_por = GetUsuariosSerializers()

    class Meta:
        model = Categorias
        fields = ('nome_categoria', 'criado_por')
