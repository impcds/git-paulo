from rest_framework import viewsets
from alunos.models import Alunos, Cursos, Matriculas
from alunos.serializer import AlunosSerializer, CursosSerializer, MatriculasSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos e alunas"""
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibe todos as matriculas"""
    queryset = Matriculas.objects.all()
    serializer_class = MatriculasSerializer

