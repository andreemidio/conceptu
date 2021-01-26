from rest_framework import serializers

from apps.categorias.serializers import ListCategoriaProdutosSerializers
from apps.produtos.models import Produtos
from apps.usuarios.serializers import GetUsuariosSerializers


class PostProdutosSerializers(serializers.ModelSerializer):
    # nome = serializers.CharField(required=True)
    # descricao = serializers.CharField(required=True)
    # preco = serializers.DecimalField(max_digits=10, decimal_places=2)
    criado_por = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Produtos
        # fields = ('id', 'nome', 'descricao' 'preco', 'criado_por')
        fields = '__all__'


class ListProdutosSerializers(serializers.ModelSerializer):
    categorias = ListCategoriaProdutosSerializers(many=True)
    criado_por = GetUsuariosSerializers()

    class Meta:
        model = Produtos
        fields = '__all__'
