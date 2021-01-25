from django.urls import path, include
from rest_framework import routers

from apps.categorias.viewsets import DeleteCategoriasViewSets
from apps.categorias.viewsets import GetCategoriasViewSets
from apps.categorias.viewsets import ListCategoriasViewSets
from apps.categorias.viewsets import PostCategoriaViewSets
from apps.categorias.viewsets import PutCategoriasViewSets

app_name = 'categorias'

router = routers.DefaultRouter()
router.register(r'criar-categoria', PostCategoriaViewSets, basename='criar-empresas')
router.register(r'listar-categorias', ListCategoriasViewSets, basename='criar-empresas')
router.register(r'detalhes-categoria', GetCategoriasViewSets, basename='criar-empresas')
router.register(r'atualizar-categoria', PutCategoriasViewSets, basename='criar-empresas')
router.register(r'deletar-categoria', DeleteCategoriasViewSets, basename='criar-empresas')

urlpatterns = [
    path(r'', include(router.urls)),
]
