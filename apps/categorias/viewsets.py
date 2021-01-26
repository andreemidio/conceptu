from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from apps.categorias.models import Categorias
from apps.categorias.serializers import ListCategoriaSerializers, RetrieveCategoriaSerializers, \
    DeleteCategoriaSerializers, PutCategoriaSerializers
from apps.categorias.serializers import PostCategoriaSerializers


class PostCategoriaViewSets(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = PostCategoriaSerializers
    queryset = Categorias.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class ListCategoriasViewSets(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ListCategoriaSerializers
    queryset = Categorias.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class GetCategoriasViewSets(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = RetrieveCategoriaSerializers
    queryset = Categorias.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class PutCategoriasViewSets(mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = PutCategoriaSerializers
    queryset = Categorias.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class DeleteCategoriasViewSets(mixins.DestroyModelMixin, GenericViewSet):
    serializer_class = DeleteCategoriaSerializers
    queryset = Categorias.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
