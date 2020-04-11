from django.contrib import admin
from .models import Cargo, Departamento, Funcionario, Veiculo, Solicitacao, Atendimento

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    pass

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    pass

@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    pass

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    pass