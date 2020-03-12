from rest_framework import serializers

from tutorialpress.core.models import Categoria, Publicacao


class PublicacaoSerializer(serializers.ModelSerializer):
    categoria = serializers.SlugRelatedField(default=None, queryset=Categoria.objects.all(), slug_field="nome")

    class Meta:
        model = Publicacao
        fields = ["id", "titulo", "conteudo", "is_publicada", "categoria"]


class PublicacaoDetailSerializer(PublicacaoSerializer):
    categoria = serializers.CharField(source="categoria.nome", default=None)
