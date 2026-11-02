from django.urls import path
from . import views


urlpatterns = [
    # Páginas institucionais do site
    path('', views.inicio, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('produtos/', views.produtos, name='produtos'),
    path('contato/', views.contato, name='contato'),

    # Consulta de informações cadastradas no banco
    path(
        'informacao/<str:titulo>/',
        views.consultar_informacao,
        name='consultar_informacao'
    ),

    # APIs do chatbot
    path(
        'api/chat/categorias/',
        views.listar_categorias_principais,
        name='listar_categorias'
    ),

    path(
        'api/chat/categoria/<str:nome_categoria>/',
        views.listar_itens_por_categoria,
        name='listar_itens_categoria'
    ),
]