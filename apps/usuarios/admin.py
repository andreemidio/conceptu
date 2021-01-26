# Register your models here.


from django.contrib import admin

from apps.usuarios.models import Usuarios


@admin.register(Usuarios)
class AssinaturasProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_sobrenome', 'cpf', 'email', 'is_superuser', 'is_staff', 'is_active', 'data_criacao')
    search_fields = ('id', 'nome', 'descricao', 'preco')
