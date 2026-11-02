
from django.db import models


class Categoria(models.Model):
    # Nome e introdução da categoria.
    nome = models.CharField(max_length=100)
    introducao = models.TextField(blank=True, default="")

    def __str__(self):
        return self.nome


class Informacao(models.Model):
    # Categoria à qual a informação pertence.
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    # Permite organizar opções dentro de outras opções.
    pai = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subitens"
    )

    # Título e resposta da informação.
    titulo = models.CharField(max_length=100)
    resposta = models.TextField()

    def __str__(self):
        return self.titulo
