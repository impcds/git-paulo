from django.http import JsonResponse


def aluno(request):
    if request.method == 'GET':
        aluno = {'id': 1, 'nome': 'Paulo'}
        return JsonResponse(aluno)
