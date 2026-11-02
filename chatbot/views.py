
from django.shortcuts import render
from django.http import JsonResponse
from .models import Categoria, Informacao


# Páginas do site
def inicio(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')


def produtos(request):
    return render(request, 'produtos.html')


def contato(request):
    return render(request, 'contato.html')


# Consulta uma informação pelo título
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


# Retorna as categorias principais do chatbot
def listar_categorias_principais(request):
    categorias = Categoria.objects.exclude(
        nome="Mensagens do chatbot"
    ).order_by('id')

    dados = [
        {
            'nome': categoria.nome,
            'introducao': categoria.introducao
        }
        for categoria in categorias
    ]

    return JsonResponse({
        'status': 'sucesso',
        'categorias': dados
    })


# Retorna as opções de uma categoria ou de um submenu
def listar_itens_por_categoria(request, nome_categoria):
    try:
        categoria = Categoria.objects.get(nome=nome_categoria)

        titulo_pai = request.GET.get('pai')

        if titulo_pai:
            pai = Informacao.objects.get(
                categoria=categoria,
                titulo=titulo_pai,
                pai__isnull=True
            )

            informacoes = Informacao.objects.filter(
                categoria=categoria,
                pai=pai
            ).order_by('id')

        else:
            informacoes = Informacao.objects.filter(
                categoria=categoria,
                pai__isnull=True
            ).order_by('id')

        itens = [
            {
                'id': item.id,
                'titulo': item.titulo,
                'resposta': item.resposta,
                'tem_subitens': item.subitens.exists()
            }
            for item in informacoes
        ]

        return JsonResponse({
            'status': 'sucesso',
            'introducao': categoria.introducao,
            'itens': itens
        })

    except Categoria.DoesNotExist:
        return JsonResponse({
            'status': 'erro',
            'mensagem': 'Categoria não encontrada.'
        }, status=404)

    except Informacao.DoesNotExist:
        return JsonResponse({
            'status': 'erro',
            'mensagem': 'Opção não encontrada.'
        }, status=404)
