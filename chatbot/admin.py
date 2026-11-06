# Importa o módulo de administração do Django.
from django.contrib import admin

# Importa os modelos que serão disponibilizados no painel administrativo.
from .models import Categoria, Informacao


# Registra o modelo Categoria no painel administrativo do Django.
# Isso permite visualizar, cadastrar, editar e excluir categorias.
admin.site.register(Categoria)

# Registra o modelo Informacao no painel administrativo.
# Assim, também podemos gerenciar as informações e respostas do chatbot.
admin.site.register(Informacao)