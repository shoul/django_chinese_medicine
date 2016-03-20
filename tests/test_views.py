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
def test_disease_detail(client):
    response = client.get(reverse('disease_detail'))
    assert 0


@pytest.mark.django_db
def test_result_detail(client):
    response = client.get(reverse('result_detail'))
    assert 0


def test_therapy_detail(client):
    response = client.get(reverse('therapy_detail'))
    assert 0


