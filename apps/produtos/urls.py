from django.urls import path, include
from rest_framework import routers

from apps.produtos.viewsets import PostProdutosViewSets
from apps.usuarios.viewsets import DeleteUsuariosViewSets, UpdateUsuariosViewSets, RetriveUsuariosViewSets, \
    ListUsuariosViewSets

app_name = 'produtos'

router = routers.DefaultRouter()
router.register(r'cadastrar-produtos', PostProdutosViewSets, basename='cadastrar-produtos')
router.register(r'listar-produtos', ListUsuariosViewSets, basename='listar-produtos')
router.register(r'detalhes-produto', RetriveUsuariosViewSets, basename='detalhes-produto')
router.register(r'atualizar-produto', UpdateUsuariosViewSets, basename='atualizar-produto')
router.register(r'deletar-produto', DeleteUsuariosViewSets, basename='deletar-produto')

urlpatterns = [
    path(r'', include(router.urls)),
]
