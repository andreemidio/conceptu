from django.urls import path, include
from rest_framework import routers

from apps.categorias.viewsets import PostCategoriaViewSets

app_name = 'categorias'

router = routers.DefaultRouter()
router.register(r'criar-categoria', PostCategoriaViewSets, basename='criar-empresas')

urlpatterns = [
    path(r'', include(router.urls)),
]
