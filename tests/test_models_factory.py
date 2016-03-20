import pytest
from django_chinese_medicine.models import Result
from django_chinese_medicine.factories import ResultFactory, EtiologieFactory


# TODO: This test fails!!!
@pytest.mark.django_db
def test_result_factory(result_factory):
    """Facktorys become fixtures automatically."""
    assert isinstance(result_factory, ResultFactory)


@pytest.mark.django_db
def test_result(result):
    """Instances become fixtures automatically."""
    assert isinstance(result, Result)


# TODO: This test fails!!!
@pytest.mark.django_db
def test_etiologie_factory(etiologie_factory):
    assert isinstance(etiologie_factory, EtiologieFactory)
