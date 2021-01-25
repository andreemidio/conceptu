from rest_framework import serializers

from apps.usuarios.models import Usuarios


class GetUsuariosSerializers(serializers.ModelSerializer):
    nome_sobrenome = serializers.CharField(required=True)
    email = serializers.EmailField()

    class Meta:
        model = Usuarios
        fields = ('nome_sobrenome', 'email')
