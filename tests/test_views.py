from django.core.urlresolvers import reverse
import pytest

from django_chinese_medicine import factories as _f


@pytest.mark.django_db
def test_main(client):
    response = client.get(reverse('main'))
    assert response.status_code == 200
    assert 'Symptome' in response.content
    assert 'Krankheitsmuster' in response.content
    assert 'Therapien' in response.content
    assert 'Etiologien' in response.content


@pytest.mark.django_db
def test_symptom_index(client):
    response = client.get(reverse('symptom_index'))
    assert response.status_code == 200
    assert 'Symptome' in response.content


@pytest.mark.django_db
def test_symptom_detail(client, symptom):
    _f.SymptomDetailFactory.create()
    response = client.get(reverse('symptom_detail',
        kwargs={'slug': 'head_pain_stinging'}))

    assert response.status_code == 200
    assert 'Head' in response.content
    assert 'head_pain_stinging' in response.content
    assert 'Pain, stinging' in response.content
    assert 'Description for stinging head pain.' in response.content


@pytest.mark.django_db
def test_disease_pattern_index(client):
    response = client.get(reverse('disease_index'))
    assert response.status_code == 200
    assert 'Krankheitsmuster' in response.content


@pytest.mark.django_db
def test_disease_pattern_detail(client, disease_pattern):
    response = client.get(reverse('disease_detail',
        kwargs={'slug': 'disease_pattern_foo'}))
    assert response.status_code == 200
    assert 'Disease pattern Foo' in response.content
    assert 'disease_pattern_foo' in response.content
    assert 'Manifestation Foo' in response.content
    assert 'Pathologie Foo' in response.content
    # TODO: Add tests for related models


@pytest.mark.django_db
def test_therapy_index(client):
    response = client.get(reverse('therapy_index'))
    assert response.status_code == 200
    assert 'Therapien' in response.content


@pytest.mark.django_db
def test_therapy_detail(client, therapy):
    response = client.get(reverse('therapy_detail',
        kwargs={'slug': 'foo_therapy'}))
    assert response.status_code == 200
    assert 'Therapie Foo' in response.content
    assert 'therapie_foo' in response.content
    assert 'Intension Foo' in response.content
    assert 'Description Foo' in response.content


@pytest.mark.django_db
def test_etiologie_index(client):
    response = client.get(reverse('etiologie_index'))
    assert response.status_code == 200
    assert 'Etiologien' in response.content


@pytest.mark.django_db
def test_etiologie_index(client, etiologie):
    _f.EtiologieDetailFactory.create()
    response = client.get(reverse('etiologie_detail',
        kwargs={'slug': 'etiologie_foo'}))
    assert response.status_code == 200
    assert 'Etiologie Foo' in response.content
    assert 'etiologie_foo' in response.content
    assert 'Description for Etiologie Foo.' in response.content

