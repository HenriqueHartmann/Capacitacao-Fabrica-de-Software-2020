from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    categoria_pai = models.ForeignKey(
        "Categoria",
        on_delete=models.SET_NULL,
        related_name="categorias",
        related_query_name="categoria",
        null=True,
        blank=True,
    )
