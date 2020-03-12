from django.urls import reverse
from rest_framework import status

import pytest
from tutorialpress.core.models import Categoria, Publicacao


@pytest.mark.django_db
def test_create_valid(api_client):
    Categoria.objects.create(nome="CS")
    dados_publicacao = {
        "titulo": "Publicacao A",
        "conteudo": "Conteudos de conteudos",
        "is_publicada": True,
        "categoria": "CS",
    }
    resp = api_client.post(reverse("publicacao-list"), dados_publicacao)
    print(resp.data)
    assert resp.status_code == status.HTTP_201_CREATED
    assert isinstance(resp.data["id"], int)
    assert Publicacao.objects.get(pk=resp.data["id"]).titulo == dados_publicacao["titulo"]


@pytest.mark.django_db
def test_create_invalid(api_client):
    dados_publicacao = {
        "titulo": "a" * 256,
        "conteudo": "Conteudos de conteudos",
    }
    resp = api_client.post(reverse("publicacao-list"), dados_publicacao)
    print(resp.data)
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    assert len(resp.data["titulo"]) != 0
    assert Publicacao.objects.count() == 0


@pytest.mark.django_db
def test_list_valid(api_client):
    resp = api_client.get(reverse("publicacao-list"))
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_retrieve_valid(api_client):
    publicacao = Publicacao.objects.create(titulo="Publicacao A", conteudo="Conteudos de conteudos",)
    resp = api_client.get(reverse("publicacao-detail", args={publicacao.id}))
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data["titulo"] == "Publicacao A"


@pytest.mark.django_db
def test_update_valid(api_client):
    publicacao = Publicacao.objects.create(titulo="Publicacao A", conteudo="Conteudos de conteudos",)
    dados_publicacao = {"titulo": "publicacao A", "conteudo": "conteudos"}
    resp = api_client.put(reverse("publicacao-detail", args={publicacao.id}), dados_publicacao)
    print(resp.data)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data["titulo"] == "publicacao A"
    assert resp.data["conteudo"] == "conteudos"


@pytest.mark.django_db
def test_destroy_valid(api_client):
    publicacao = Publicacao.objects.create(titulo="Publicacao A", conteudo="Conteudos de conteudos",)
    resp = api_client.delete(reverse("publicacao-detail", args={publicacao.id}))
    assert resp.status_code == status.HTTP_204_NO_CONTENT
