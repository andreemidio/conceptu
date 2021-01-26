from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.produtos.models import Produtos
from apps.produtos.serializers import PostProdutosSerializers, ListProdutosSerializers, RetriveProdutosSerializers, \
    UpdateProdutosSerializers


class PostProdutosViewSets(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = PostProdutosSerializers
    queryset = Produtos.objects.all()


class ListProdutosViewSets(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ListProdutosSerializers
    queryset = Produtos.objects.all()


class RetriveProdutosViewSets(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = RetriveProdutosSerializers
    queryset = Produtos.objects.all()


class UpdateProdutosViewSets(mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = UpdateProdutosSerializers
    queryset = Produtos.objects.all()


class DestroyProdutosViewSets(mixins.DestroyModelMixin, GenericViewSet):
    serializer_class = ListProdutosSerializers
    queryset = Produtos.objects.all()
