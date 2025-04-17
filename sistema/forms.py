from django import forms
from .models import Paciente
from .models import Medico

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [ 'nome', 'sobrenome', 'email', 'telefone',]


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'crm', 'especialidade_id',]