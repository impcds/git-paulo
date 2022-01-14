from rest_framework import serializers
from alunos.models import Alunos, Cursos


class AlunosSerializer(serializers.Serializer):
    class Meta:
        models = Alunos
        fields = ['id', 'rg', 'cpf', 'data_nascimento']


class CursosSerializer(serializers.Serializer):
    class Meta:
        models = Cursos
        fields = '__all__'
        