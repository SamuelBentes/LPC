from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Solicitacao, Veiculo, Funcionario


def todas_solicitacoes(request):
    todas = Solicitacao.objects.all()
    return render(request, 'app_transporte/solicitacao.html', {'todas_solicitacao':todas})


def detalhe_solicitacao(request, datalheSolicitacao_id):
    try:
        detalhesolicitacao = Solicitacao.objects.get(pk=datalheSolicitacao_id)
        return render(request, 'app_transporte/detalhe_solicitacao.html', {'detalhesolicitacao':detalhesolicitacao})
    except Exception:
        raise Http404('Página não encontada')
    
    return render(request, 'app_transporte/detalhe_solicitacao.html', {'detalhesolicitacao':detalhesolicitacao})

def todos_carros(request):
    todos = Veiculo.objects.all()
    return render(request, 'app_transporte/veiculo.html', {'todo_carro':todos})


def detalhe_carro(request, detalheCarro_id):
    try:
        detalhecarro = Veiculo.objects.get(pk=detalheCarro_id)
        return render(request, 'app_transporte/detalhe_carro.html', {'detalhecarro':detalhecarro})
    except Exception:
        raise Http404('Página não encontada')
    
    return render(request, 'app_transporte/detalhe_carro.html', {'detalhecarro':detalhecarro})

def todos_funcionarios(request):
    todos = Funcionario.objects.all()
    return render(request, 'app_transporte/funcionario.html', {'todo_funcionario':todos})


def detalhe_funcionario(request, detalheFuncionario_id):
    try:
        detalhefuncionario = Funcionario.objects.get(pk=detalheFuncionario_id)
        return render(request, 'app_transporte/detalhe_funcionario.html', {'detalhefuncionario':detalhefuncionario})
    except Exception:
        raise Http404('Página não encontada')
    
    return render(request, 'app_transporte/detalhe_funcionario.html', {'detalhefuncionario':detalhefuncionario})
