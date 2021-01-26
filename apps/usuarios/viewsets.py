from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from apps.usuarios.models import Usuarios
from apps.usuarios.serializers import PostUsuariosSerializers, GetUsuariosSerializers


class PostUsuariosViewSets(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = PostUsuariosSerializers
    permission_classes = (permissions.AllowAny,)


class ListUsuariosViewSets(mixins.ListModelMixin, GenericViewSet):
    serializer_class = GetUsuariosSerializers
    queryset = Usuarios.objects.all()


class RetriveUsuariosViewSets(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = GetUsuariosSerializers
    queryset = Usuarios.objects.all()


class UpdateUsuariosViewSets(mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = GetUsuariosSerializers
    queryset = Usuarios.objects.all()


class DeleteUsuariosViewSets(mixins.DestroyModelMixin, GenericViewSet):
    serializer_class = GetUsuariosSerializers
    queryset = Usuarios.objects.all()
