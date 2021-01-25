from django.urls import path, include
from rest_framework import routers

from apps.produtos.viewsets import PostProdutosViewSets

app_name = 'produtos'

router = routers.DefaultRouter()
router.register(r'cadastrar-produtos', PostProdutosViewSets, basename='cadastrar-produtos')

urlpatterns = [
    path(r'', include(router.urls)),
]
