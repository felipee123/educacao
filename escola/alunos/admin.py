from django.contrib import admin # type: ignore
from .models import Aluno, Curso

admin.site.register(Aluno)
admin.site.register(Curso)
