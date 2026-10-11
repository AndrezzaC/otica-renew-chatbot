
from django.shortcuts import render
from django.http import JsonResponse
from .models import Informacao


# Exibe a página inicial do site.
def inicio(request):
    return render(request, 'index.html')


# Exibe a página Sobre.
def sobre(request):
    return render(request, 'sobre.html')


# Exibe a página de Produtos.
def produtos(request):
    return render(request, 'produtos.html')


# Exibe a página de Contato.
def contato(request):
    return render(request, 'contato.html')


# Consulta uma informação cadastrada no banco usando o ORM.
def consultar_informacao(request, titulo):
    informacao = Informacao.objects.select_related(
        'categoria'
    ).filter(titulo=titulo).first()

    if informacao is None:
        return JsonResponse(
            {'erro': 'Informação não encontrada.'},
            status=404
        )

    return JsonResponse({
        'titulo': informacao.titulo,
        'categoria': informacao.categoria.nome,
        'resposta': informacao.resposta
    })