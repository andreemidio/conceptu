# Register your models here.


from django.contrib import admin

from apps.produtos.models import Produtos


@admin.register(Produtos)
class AssinaturasProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'preco')
    search_fields = ('id', 'nome', 'descricao', 'preco')
