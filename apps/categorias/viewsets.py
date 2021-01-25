import logging

from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.categorias.serializers import PostCategoriaSerializers


class PostCategoriaViewSets(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = PostCategoriaSerializers

    def create(self, request, *args, **kwargs):
        try:

            request.data['criado_por'] = request.user.id
            serializer = PostCategoriaSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        except Exception as error:
            logging.error(error)

            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ListCategoriasViewSets(mixins.ListModelMixin, GenericViewSet):
    pass


class GetCategoriasViewSets(mixins.RetrieveModelMixin, GenericViewSet):
    pass


class PutCategoriasViewSets(mixins.UpdateModelMixin, GenericViewSet):
    pass


class DeleteCategoriasViewSets(mixins.DestroyModelMixin, GenericViewSet):
    pass
