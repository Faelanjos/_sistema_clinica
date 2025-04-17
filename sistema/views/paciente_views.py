from django.shortcuts import render, redirect, get_object_or_404
from sistema.forms import PacienteForm
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

#View referente a criação do paciente
def criarPaciente(request):
    if request.method == 'POST':

        form = PacienteForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/pacientes')
        
    else:

        form = PacienteForm()

    return render(
        request,
        'paciente/cadastro.html',
        {'form': form}
    )


#View referente aos detalhes(perfil) do paciente
def perfilPaciente(request, paciente_id):
    pacienteUnico = get_object_or_404( #método utilizado para mostrar o paciente ou exibir erro 404
        Paciente, pk=paciente_id #Paciente é o model, pc=paciente_id está definido através de qual campo(coluna) o objeto será retornado
    )
    titulo = f'{pacienteUnico.nome} {pacienteUnico.sobrenome}' #Cria um título com nome e sobranome do paciente atual
    context = { #declaração de um dict que possui a chave pacientes e o valor pacientes (variavel criada acima)
        'pacienteUnico' : pacienteUnico,
        'titulo': titulo,
    }


    return render(
        request,
        'paciente/perfil.html',
        context,

    )
