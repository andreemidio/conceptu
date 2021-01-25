from django.urls import path, include
from rest_framework import routers

from apps.usuarios.viewsets import PostUsuariosViewSets

app_name = 'usuarios'

router = routers.DefaultRouter()
router.register(r'cadastrar-usuarios', PostUsuariosViewSets, basename='cadastrar-usuarios')

urlpatterns = [
    path(r'', include(router.urls)),
]