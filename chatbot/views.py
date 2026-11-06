# Importa a função render, utilizada para carregar e apresentar páginas HTML.
from django.shortcuts import render

# Importa JsonResponse, utilizado para retornar dados no formato JSON.
from django.http import JsonResponse

# Importa os modelos que permitem consultar as informações do banco de dados.
from .models import Categoria, Informacao


# Páginas do site

# Função responsável por apresentar a página inicial.
# request representa a requisição recebida pelo Django.
def inicio(request):
    # Renderiza o arquivo HTML da página inicial.
    return render(request, 'index.html')


# Função responsável por apresentar a página sobre.
def sobre(request):
    return render(request, 'sobre.html')


# Função responsável por apresentar a página de produtos.
def produtos(request):
    return render(request, 'produtos.html')


# Função responsável por apresentar a página de contato.
def contato(request):
    return render(request, 'contato.html')


# Consulta uma informação pelo título.
# O título é recebido como parâmetro pela URL.
def consultar_informacao(request, titulo):

    # Consulta o banco de dados procurando uma informação com o título recebido.
    # select_related('categoria') busca também a categoria relacionada,
    # evitando uma consulta adicional ao banco quando acessarmos seu nome.
    # filter() aplica o filtro pelo título.
    # first() retorna o primeiro resultado encontrado ou None se não existir.
    informacao = Informacao.objects.select_related(
        'categoria'
    ).filter(titulo=titulo).first()

    # Verifica se nenhuma informação foi encontrada no banco de dados.
    if informacao is None:

        # Retorna uma resposta JSON informando que o registro não foi encontrado.
        # O status HTTP 404 representa recurso não encontrado.
        return JsonResponse(
            {'erro': 'Informação não encontrada.'},
            status=404
        )

    # Se a informação existir, retorna seus dados no formato JSON.
    # O front-end poderá utilizar esses dados para apresentar a resposta.
    return JsonResponse({
        'titulo': informacao.titulo,
        'categoria': informacao.categoria.nome,
        'resposta': informacao.resposta
    })


# Retorna as categorias principais do chatbot.
def listar_categorias_principais(request):

    # Consulta as categorias cadastradas no banco.
    # exclude() remove da consulta a categoria interna de mensagens do chatbot.
    # order_by('id') organiza os resultados pelo identificador.
    categorias = Categoria.objects.exclude(
        nome="Mensagens do chatbot"
    ).order_by('id')

    # Percorre as categorias encontradas e monta uma lista de dicionários.
    # Cada dicionário contém o nome e a introdução de uma categoria.
    dados = [
        {
            'nome': categoria.nome,
            'introducao': categoria.introducao
        }
        for categoria in categorias
    ]

    # Retorna os dados no formato JSON.
    # O status indica que a consulta foi realizada com sucesso.
    return JsonResponse({
        'status': 'sucesso',
        'categorias': dados
    })


# Retorna as opções de uma categoria ou de um submenu.
# nome_categoria é recebido como parâmetro pela URL.
def listar_itens_por_categoria(request, nome_categoria):

    # try permite executar uma operação que pode gerar uma exceção.
    # Nesse caso, tentamos localizar a categoria no banco de dados.
    try:

        # Busca uma categoria pelo nome informado na URL.
        # get() espera encontrar exatamente um registro.
        categoria = Categoria.objects.get(nome=nome_categoria)

        # Lê o parâmetro chamado "pai" enviado na URL por uma requisição GET.
        # Ele é utilizado para identificar se o usuário está acessando um submenu.
        titulo_pai = request.GET.get('pai')

        # Verifica se foi informado um título de item pai.
        if titulo_pai:

            # Localiza a opção principal que será utilizada como item pai.
            # A busca considera a categoria, o título e verifica se o item
            # não possui outro pai, ou seja, se é uma opção principal.
            pai = Informacao.objects.get(
                categoria=categoria,
                titulo=titulo_pai,
                pai__isnull=True
            )

            # Busca somente as informações que pertencem ao item pai encontrado.
            # A consulta utiliza a categoria e o relacionamento pai.
            # order_by('id') organiza os resultados pelo identificador.
            informacoes = Informacao.objects.filter(
                categoria=categoria,
                pai=pai
            ).order_by('id')

        # Caso não exista um parâmetro "pai", buscamos as opções principais.
        else:

            # Busca as informações da categoria que não possuem item pai.
            # pai__isnull=True identifica os registros sem relacionamento pai.
            informacoes = Informacao.objects.filter(
                categoria=categoria,
                pai__isnull=True
            ).order_by('id')

        # Percorre as informações encontradas e monta uma lista de dicionários.
        # Cada dicionário contém os dados necessários para o front-end.
        itens = [
            {
                # Identificador do registro no banco de dados.
                'id': item.id,

                # Título da opção exibida no chatbot.
                'titulo': item.titulo,

                # Resposta cadastrada para aquela opção.
                'resposta': item.resposta,

                # Verifica se a informação possui itens filhos.
                # exists() retorna True se existir pelo menos um subitem,
                # ou False caso não exista nenhum.
                'tem_subitens': item.subitens.exists()
            }
            for item in informacoes
        ]

        # Retorna os dados da categoria e suas opções em formato JSON.
        return JsonResponse({
            'status': 'sucesso',
            'introducao': categoria.introducao,
            'itens': itens
        })

    # Trata o erro caso a categoria informada não exista no banco.
    except Categoria.DoesNotExist:

        # Retorna uma mensagem de erro e o status HTTP 404.
        return JsonResponse({
            'status': 'erro',
            'mensagem': 'Categoria não encontrada.'
        }, status=404)

    # Trata o erro caso a opção principal informada não seja encontrada.
    except Informacao.DoesNotExist:

        # Retorna uma mensagem de erro e o status HTTP 404.
        return JsonResponse({
            'status': 'erro',
            'mensagem': 'Opção não encontrada.'
        }, status=404)