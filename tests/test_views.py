from django.core.urlresolvers import reverse
import pytest
from django_chinese_medicine.views import SymptomIndex


@pytest.mark.django_db
def test_main(client):
    response = client.get(reverse('main'))
    assert response.status_code == 200
    assert 'Symptome' in response.content
    assert 'Syndrome' in response.content
    assert 'Therapien' in response.content


@pytest.mark.django_db
def test_symptom_index(client):
    response = client.get(reverse('symptom_index'))
    assert response.status_code == 200
    assert 'Symptome' in response.content


@pytest.mark.django_db
def test_disease_index(client):
    response = client.get(reverse('disease_index'))
    assert response.status_code == 200
    assert 'Syndrome' in response.content


@pytest.mark.django_db
def test_therapy_index(client):
    response = client.get(reverse('therapy_index'))
    assert response.status_code == 200
    assert 'Therapien' in response.content


@pytest.mark.django_db
def test_disease_pattern_detail(client, disease_pattern):
    response = client.get(reverse('disease_detail',
        kwargs={'slug': 'foo_disease_pattern'}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_symptom_detail(client, symptom):
    response = client.get(reverse('symptom_detail',
        kwargs={'slug': 'foo_symptom'}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_therapy_detail(client, therapy):
    response = client.get(reverse('therapy_detail',
        kwargs={'slug': 'foo_therapy'}))
    assert response.status_code == 200


