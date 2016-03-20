from pytest_factoryboy import register

from django_chinese_medicine.factories import (ResultFactory, EtiologieFactory,
        DiseasePatternFactory, TherapyFactory)

register(ResultFactory)
register(EtiologieFactory)
register(DiseasePatternFactory)
register(TherapyFactory)
