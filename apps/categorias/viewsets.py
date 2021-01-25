from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class PostCategoriaViewSets(mixins.CreateModelMixin, GenericViewSet):
    pass
