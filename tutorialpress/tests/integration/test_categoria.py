import pytest
from django.urls import reverse
from rest_framework import status

from tutorialpress.core.models import Categoria


@pytest.mark.django_db
def test_create_valid(api_client):
    dados_categoria = {"nome": "Categoria A"}
    resp = api_client.post(reverse("categoria-list"), dados_categoria)
    assert resp.status_code == status.HTTP_201_CREATED
    assert isinstance(resp.data["id"], int)
    assert Categoria.objects.get(pk=resp.data["id"]).nome == dados_categoria["nome"]


@pytest.mark.django_db
def test_create_invalid(api_client):
    dados_categoria = {"novoCampo": "valorNovo"}
    resp = api_client.post(reverse("categoria-list"), dados_categoria)
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    assert len(resp.data["nome"]) != 0
    assert Categoria.objects.count() == 0


@pytest.mark.django_db
def test_list_valid(api_client):
    resp = api_client.get(reverse("categoria-list"))
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_retrieve_valid(api_client):
    categoria = Categoria.objects.create(nome="categoria1")
    resp = api_client.get(reverse("categoria-detail", args={categoria.id}))
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_valid(api_client):
    categoria = Categoria.objects.create(nome="categoria1")
    dados_categoria = {"nome": "Categoria A"}
    resp = api_client.put(reverse("categoria-detail", args={categoria.id}), dados_categoria)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data["nome"] == "Categoria A"


@pytest.mark.django_db
def test_destroy_valid(api_client):
    categoria = Categoria.objects.create(nome="categoria1")
    resp = api_client.delete(reverse("categoria-detail", args={categoria.id}))
    assert resp.status_code == status.HTTP_204_NO_CONTENT
