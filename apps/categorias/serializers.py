from rest_framework import serializers

from apps.categorias.models import Categorias
from apps.usuarios.serializers import GetUsuariosSerializers


class PostCategoriaSerializers(serializers.ModelSerializer):
    nome_categoria = serializers.CharField(required=True)
    criado_por = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Categorias
        fields = ('nome_categoria', 'criado_por')


class ListCategoriaSerializers(serializers.ModelSerializer):
    nome_categoria = serializers.CharField(required=True)
    criado_por = GetUsuariosSerializers()

    class Meta:
        model = Categorias
        fields = ('nome_categoria', 'criado_por')
