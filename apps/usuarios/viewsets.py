from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from apps.usuarios.models import Usuarios
from apps.usuarios.serializers import PostUsuariosSerializers, GetUsuariosSerializers, UpdateUsuariosSerializers, \
    RetrieveUsuariosSerializers


class PostUsuariosViewSets(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = PostUsuariosSerializers
    permission_classes = (permissions.AllowAny,)


class ListUsuariosViewSets(mixins.ListModelMixin, GenericViewSet):
    serializer_class = GetUsuariosSerializers
    queryset = Usuarios.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class RetriveUsuariosViewSets(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = RetrieveUsuariosSerializers
    queryset = Usuarios.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class UpdateUsuariosViewSets(mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = UpdateUsuariosSerializers
    queryset = Usuarios.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class DeleteUsuariosViewSets(mixins.DestroyModelMixin, GenericViewSet):
    serializer_class = GetUsuariosSerializers
    queryset = Usuarios.objects.all()
    permission_classes = (permissions.IsAdminUser,)
