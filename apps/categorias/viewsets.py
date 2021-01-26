from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.categorias.models import Categorias
from apps.categorias.serializers import ListCategoriaSerializers
from apps.categorias.serializers import PostCategoriaSerializers


class PostCategoriaViewSets(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = PostCategoriaSerializers


class ListCategoriasViewSets(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ListCategoriaSerializers
    queryset = Categorias.objects.all()


class GetCategoriasViewSets(mixins.RetrieveModelMixin, GenericViewSet):
    pass


class PutCategoriasViewSets(mixins.UpdateModelMixin, GenericViewSet):
    pass


class DeleteCategoriasViewSets(mixins.DestroyModelMixin, GenericViewSet):
    pass
