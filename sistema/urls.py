#São as importações realizadas de forma a utilizar partes do Django

from django.urls import path

# Importação do modulo views.py onde tem a view da index
from sistema import views


app_name = 'sistema'

#Lista responsável por organizar as urls do sistema
urlpatterns = [
    path('', views.index, name='index'),
]

#path() -> é um método do Django que permite realizar a inserção de uma uma URL