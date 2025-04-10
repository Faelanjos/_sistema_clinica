#São as importações realizadas de forma a utilizar partes do Django

from django.urls import path

# Importação do diretório views.py onde tem a view da index e a view listarPacientes
from sistema import views


app_name = 'sistema'

#Lista responsável por organizar as urls do sistema
urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', views.listarPacientes, name='pacientes'),
    path('medicos/', views.listarMedicos, name='medicos')
]

#path() -> é um método do Django que permite realizar a inserção de uma uma URL