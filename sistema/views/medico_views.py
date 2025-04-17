from django.shortcuts import render, redirect
from sistema.forms import MedicoForm
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

def criarMedico(request):
    if request.method == 'POST':

        form = MedicoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/medicos')
        
    else:

        form = MedicoForm()

    return render(
        request,
        'medico/cadastro.html',
        {'form': form}
    )