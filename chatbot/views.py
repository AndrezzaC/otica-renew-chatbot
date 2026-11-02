
from django.shortcuts import render
from django.http import JsonResponse
from .models import Categoria, Informacao


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

# Retorna as categorias principais do chatbot.
def listar_categorias_principais(request):
    categorias = Categoria.objects.exclude(
        nome="Mensagens do chatbot"
    ).values_list("nome", flat=True)

    return JsonResponse({
        "status": "sucesso",
        "categorias": list(categorias)
    })


# Retorna os tópicos cadastrados em uma categoria.
def listar_itens_por_categoria(request, nome_categoria):
    try:
        categoria = Categoria.objects.get(nome=nome_categoria)

        informacoes = Informacao.objects.filter(
            categoria=categoria
        ).values("titulo", "resposta")

        return JsonResponse({
            "status": "sucesso",
            "itens": list(informacoes)
        })

    except Categoria.DoesNotExist:
        return JsonResponse({
            "status": "erro",
            "mensagem": "Categoria não encontrada."
        }, status=404)