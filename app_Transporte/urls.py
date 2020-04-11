from django.urls import path

from .views import todas_solicitacoes, detalhe_solicitacao, detalhe_carro, todos_carros, detalhe_funcionario, todos_funcionarios

urlpatterns = [
    path('detalhe_solicitacao', todas_solicitacoes, name='inicio'),
    path('detalhe_solicitacao/<int:datalheSolicitacao_id>/', detalhe_solicitacao, name='detalhe_solicitacao'),

    path('detalhe_carro', todos_carros, name='inicio'),
    path('detalhe_carro/<int:detalheCarro_id>/', detalhe_carro, name='detalhe_carro'),

    path('detalhe_funcionario', todos_funcionarios, name='inicio'),
    path('detalhe_funcionario/<int:detalheFuncionario_id>/', detalhe_funcionario, name='detalhe_funcionario'),
]
