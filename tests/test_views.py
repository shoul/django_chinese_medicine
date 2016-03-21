from django.core.urlresolvers import reverse
import pytest
from django_chinese_medicine.views import ResultIndex


@pytest.mark.django_db
def test_result_index(client):
    response = client.get(reverse('result_index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_disease_list(client):
    response = client.get(reverse('disease_index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_disease_pattern_detail(client, disease_pattern):
    response = client.get(reverse('disease_detail',
        kwargs={'slug': 'foo_disease_pattern'}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_result_detail(client, result):
    response = client.get(reverse('result_detail',
        kwargs={'slug': 'foo_result'}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_therapy_detail(client, therapy):
    response = client.get(reverse('therapy_detail',
        kwargs={'slug': 'foo_therapy'}))
    assert response.status_code == 200


