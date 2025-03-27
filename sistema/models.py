# Importação do módulo models que traz métodos do banco de dados 
from django.db import models

# Importação do módulo Timezone, que traz datas e horarios.
from django.utils import timezone

# Aqui fica o model do paciente.
class Paciente(models.Model):
    nome = models.CharField(max_length = 50)
    sobrenome = models.CharField(max_length = 50)
    email = models.EmailField()
    telefone = models.CharField(max_length = 20)
    criacao_data = models.DateTimeField(default=timezone.now)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/%Y/%m/', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


#aqui fica o model da especialidade
class Especialidade(models.Model):
    nome = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.nome}'
    
#Aqui fica o model do Medico
class Medico(models.Model):
    nome = models.CharField(max_length = 50)
    sobrenome = models.CharField(max_length = 50)
    crm = models.CharField(max_length = 20)
    email = models.EmailField()
    cadastro_data = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length = 20)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/med/%Y/%m/', blank=True)
    especialidade = models.ForeignKey(Especialidade, default='1', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
    
class Consulta(models.Model):
    agendamento = models.DateTimeField()
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    status = models.CharField(default='A', max_length=1, 
                                  choices=(
                                           ('A','Agendada'),
                                           ('C','Cancelada'),
                                           ('M', 'Confirmada'),
                                           ('R','Realizada'),
                                           )
                                           )
    observacao = models.TextField(blank=True,)


    def __str__(self):
        return f'Consulta {self.status} na data {self.agendamento}'
    
