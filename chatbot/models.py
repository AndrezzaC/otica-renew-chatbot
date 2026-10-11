
from django.db import models


class Categoria(models.Model):
    # Guarda o nome de cada categoria do chatbot.
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Informacao(models.Model):
    # Relaciona a informação à sua categoria.
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    # Guarda o identificador da informação.
    titulo = models.CharField(max_length=100)

    # Guarda o texto que o chatbot apresentará.
    resposta = models.TextField()

    def __str__(self):
        return self.titulo