from django.contrib import admin

# Importação do módulo models.py
from sistema import models


# Aqui fica o registro do model do paciente.
@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'ativo',)
    list_editable = ('ativo',)
    search_fields = ('id', 'nome', 'sobrenome', 'email',)


@admin.register(models.Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('id','nome',)
    search_fields = ('nome',)

@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'crm', 'email', 'telefone', 'ativo', 'especialidade')
    list_editable = ('ativo',)
    search_fields = ('id', 'nome', 'sobrenome', 'email', 'crm', )


@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'agendamento', 'id_medico', 'id_paciente', 'status',)
    list_editable = ('status',)
    search_fields = ('data',)