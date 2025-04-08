from django.shortcuts import render
from sistema.models import Paciente

def listarPacientes(request):
    pacientes = Paciente.objects.all() #Variavel pacientes está guardando todos os objetos da tabela Pacientes

    context = { #declaração de um dict que possui a chave pacientes e o valor pacientes (variavel criada acima)
        'pacientes' : pacientes,
    }
    
    return render(
        request,
        'paciente/listar.html',
        context,

    )