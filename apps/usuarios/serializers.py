from rest_framework import serializers

from apps.usuarios.models import Usuarios


class PostUsuariosSerializers(serializers.ModelSerializer):
    nome_sobrenome = serializers.CharField(required=True)
    cpf = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Usuarios
        fields = ('nome_sobrenome', 'email', 'cpf')


class GetUsuariosSerializers(serializers.ModelSerializer):
    nome_sobrenome = serializers.CharField(required=True)
    cpf = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Usuarios
        fields = ('nome_sobrenome', 'email', 'cpf')
