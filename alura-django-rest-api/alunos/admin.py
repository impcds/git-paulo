from django.contrib import admin
from alunos.models import Alunos, Cursos, Matriculas
# Register your models here.


class Aluno(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_per_page = 20


admin.site.register(Alunos, Aluno)

class Curso(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)


admin.site.register(Cursos, Curso)


class Matricula(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_editable = ('periodo', )


admin.site.register(Matriculas, Matricula)
