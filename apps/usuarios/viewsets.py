from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class PostUsuariosViewSets(mixins.CreateModelMixin, GenericViewSet):
    pass
