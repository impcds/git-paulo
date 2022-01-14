from rest_framework import serializers
from alunos.models import Alunos, Cursos


class AlunosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alunos
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cursos
        fields = '__all__'

