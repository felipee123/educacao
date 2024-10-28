
from django.urls import path # type: ignore
from .views import lista_alunos, lista_cursos  # Certifique-se de que ambas as views foram importadas

urlpatterns = [
    path('alunos/', lista_alunos, name='lista_alunos'),
    path('cursos/', lista_cursos, name='lista_cursos'),
]
