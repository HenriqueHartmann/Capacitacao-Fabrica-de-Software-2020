from rest_framework import serializers

from tutorialpress.core.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    categoria_pai = serializers.SlugRelatedField(default=None, queryset=Categoria.objects.all(), slug_field="nome")

    class Meta:
        model = Categoria
        fields = ["id", "nome", "categoria_pai"]
