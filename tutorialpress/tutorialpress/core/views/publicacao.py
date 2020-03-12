from rest_framework import viewsets

from tutorialpress.core.models import Publicacao
from tutorialpress.core.serializers import PublicacaoDetailSerializer, PublicacaoSerializer


class PublicacaoViewSet(viewsets.ModelViewSet):
    queryset = Publicacao.objects.all()
    lookup_field = "id"
    # serializer_class = PublicacaoSerializer

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            return PublicacaoDetailSerializer(*args, **kwargs)
        else:
            return PublicacaoSerializer(*args, **kwargs)
