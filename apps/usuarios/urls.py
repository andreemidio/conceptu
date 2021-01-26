from django.urls import path, include
from rest_framework import routers

from apps.usuarios.viewsets import PostUsuariosViewSets, ListUsuariosViewSets, UpdateUsuariosViewSets, \
    RetriveUsuariosViewSets, DeleteUsuariosViewSets

app_name = 'usuarios'

router = routers.DefaultRouter()
router.register(r'cadastrar-usuarios', PostUsuariosViewSets, basename='cadastrar-usuarios')
router.register(r'listar-usuarios', ListUsuariosViewSets, basename='cadastrar-usuarios')
router.register(r'detalhes-usuario', RetriveUsuariosViewSets, basename='cadastrar-usuarios')
router.register(r'atualizar-usuario', UpdateUsuariosViewSets, basename='cadastrar-usuarios')
router.register(r'deletar-usuario', DeleteUsuariosViewSets, basename='cadastrar-usuarios')

urlpatterns = [
    path(r'', include(router.urls)),
]
