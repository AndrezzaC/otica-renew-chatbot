
from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('produtos/', views.produtos, name='produtos'),
    path('contato/', views.contato, name='contato'),
    path(
        'informacao/<str:titulo>/',
        views.consultar_informacao,
        name='consultar_informacao'
    ),
]