# Register your models here.


from django.contrib import admin

from apps.categorias.models import Categorias


@admin.register(Categorias)
class AssinaturasProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria', 'criado_por')
    search_fields = ('id', 'nome_categoria', 'criado_por')
