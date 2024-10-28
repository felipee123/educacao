from django.shortcuts import render # type: ignore
from .models import Aluno, Curso  # Verifique se você importou os modelos necessários

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})

# Verifique se esta função está definida
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'alunos/lista_cursos.html', {'cursos': cursos})