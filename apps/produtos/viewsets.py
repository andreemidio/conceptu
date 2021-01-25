from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class PostProdutosViewSets(mixins.CreateModelMixin, GenericViewSet):
    pass
