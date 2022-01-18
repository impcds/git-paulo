from rest_framework import viewsets, generics
from alunos.models import Alunos, Cursos, Matriculas
from alunos.serializer import AlunosSerializer, CursosSerializer, MatriculasSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos e alunas"""
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibe todos as matriculas"""
    queryset = Matriculas.objects.all()
    serializer_class = MatriculasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas de um anluno(a)"""
    def get_queryset(self):
        queryset = Matriculas.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """Lista todos alunos(as) matriculados em um curso"""
    def get_queryset(self):
        queryset = Matriculas.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaCursos(generics.ListAPIView):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer
