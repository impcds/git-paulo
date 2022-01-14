from rest_framework import viewsets
from alunos.models import Alunos, Cursos
from alunos.serializer import AlunosSerializer, CursosSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos e alunas"""
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

