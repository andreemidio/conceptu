from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.usuarios.models import Usuarios


class PostUsuariosSerializers(serializers.ModelSerializer):
    nome_sobrenome = serializers.CharField(required=True)
    cpf = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Usuarios
        fields = ('nome_sobrenome', 'email', 'cpf', 'password')
        read_only_fields = ('is_active', 'is_staff')
        extra_kwargs = {
            'security_question': {'write_only': True},
            'security_question_answer': {'write_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super(PostUsuariosSerializers, self).create(validated_data)


class GetUsuariosSerializers(serializers.ModelSerializer):
    nome_sobrenome = serializers.CharField(required=True)
    cpf = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Usuarios
        fields = ('id', 'nome_sobrenome', 'email', 'cpf')


class RetrieveUsuariosSerializers(serializers.ModelSerializer):
    nome_sobrenome = serializers.CharField(required=True)
    cpf = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Usuarios
        fields = ('id', 'nome_sobrenome', 'email', 'cpf')


class UpdateUsuariosSerializers(serializers.ModelSerializer):
    id = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    nome_sobrenome = serializers.CharField(required=True)
    cpf = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Usuarios
        fields = ('id', 'nome_sobrenome', 'email', 'cpf')
