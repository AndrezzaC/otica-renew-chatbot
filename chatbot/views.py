
from django.shortcuts import render

# o render recebe a solicitação do navegador e entrega o HTML correspondente

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
