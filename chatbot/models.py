# Importa o módulo de modelos do Django, utilizado para criar tabelas e campos no banco.
from django.db import models


# Modelo responsável por representar as categorias principais do chatbot.
class Categoria(models.Model):

    # Campo de texto curto para armazenar o nome da categoria.
    # max_length define o limite máximo de caracteres.
    nome = models.CharField(max_length=100)

    # Campo de texto longo para armazenar uma introdução da categoria.
    # blank=True permite que o campo fique vazio nos formulários.
    # default="" define um texto vazio como valor padrão.
    introducao = models.TextField(blank=True, default="")

    # Define como o objeto será representado quando convertido para texto.
    # Nesse caso, será exibido o nome da categoria.
    def __str__(self):
        return self.nome


# Modelo responsável por armazenar as perguntas, opções e respostas do chatbot.
class Informacao(models.Model):

    # Cria um relacionamento entre Informacao e Categoria.
    # ForeignKey representa uma relação em que várias informações
    # podem pertencer a uma mesma categoria.
    # on_delete=models.CASCADE determina que, se uma categoria for excluída,
    # as informações relacionadas a ela também serão excluídas.
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    # Cria um relacionamento do modelo Informacao com ele mesmo.
    # Isso permite que uma informação tenha outra informação como item pai,
    # organizando opções e subopções dentro do chatbot.
    # null=True permite que o campo seja nulo no banco de dados.
    # blank=True permite que ele fique vazio nos formulários.
    # related_name="subitens" permite acessar os itens filhos por meio
    # do relacionamento inverso, utilizando pai.subitens.
    pai = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subitens"
    )

    # Campo de texto curto que armazena o título da opção ou pergunta.
    titulo = models.CharField(max_length=100)

    # Campo de texto longo que armazena a resposta apresentada ao usuário.
    resposta = models.TextField()

    # Define que a representação textual de uma informação será seu título.
    def __str__(self):
        return self.titulo