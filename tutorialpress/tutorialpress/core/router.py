from rest_framework import routers

from tutorialpress.core.views.publicacao import PublicacaoViewSet

router = routers.SimpleRouter()
router.register("publicacoes", PublicacaoViewSet)
