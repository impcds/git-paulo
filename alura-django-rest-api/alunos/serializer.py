from rest_framework import serializers
from alunos.models import Alunos, Cursos, Matriculas


class AlunosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alunos
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cursos
        fields = '__all__'


class MatriculasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Matriculas
        fields = '__all__'


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matriculas
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.rg')

    class Meta:
        model = Matriculas
        fields = ['aluno_nome']