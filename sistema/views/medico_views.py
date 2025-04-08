from django.shortcuts import render
from sistema.models import Medico

def listarMedicos(request):
    medicos = Medico.objects.all() #Variavel pacientes está guardando todos os objetos da tabela Pacientes

    context = { #declaração de um dict que possui a chave pacientes e o valor pacientes (variavel criada acima)
        'medicos' : medicos,
    }
    
    return render(
        request,
        'medico/listar.html',
        context,

    )