# Importa a função path, utilizada para definir as rotas do Django.
from django.urls import path

# Importa o arquivo views do próprio aplicativo.
# As funções responsáveis por processar as requisições estão nele.
from . import views


# Lista que reúne todas as rotas disponíveis neste aplicativo.
urlpatterns = [

    # Páginas institucionais do site.
    # Cada rota direciona a requisição para uma função específica em views.py.
    path('', views.inicio, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('produtos/', views.produtos, name='produtos'),
    path('contato/', views.contato, name='contato'),

    # Consulta uma informação cadastrada no banco de dados.
    # <str:titulo> captura um texto da URL e o envia como parâmetro para a view.
    path(
        'informacao/<str:titulo>/',
        views.consultar_informacao,
        name='consultar_informacao'
    ),

    # APIs utilizadas pelo chatbot.
    # Essa rota disponibiliza as categorias principais para o front-end.
    path(
        'api/chat/categorias/',
        views.listar_categorias_principais,
        name='listar_categorias'
    ),

    # Essa rota recebe o nome de uma categoria pela URL
    # e retorna as opções cadastradas nela.
    path(
        'api/chat/categoria/<str:nome_categoria>/',
        views.listar_itens_por_categoria,
        name='listar_itens_categoria'
    ),
]