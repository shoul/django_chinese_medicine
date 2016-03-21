from pytest_factoryboy import register

from django_chinese_medicine.factories import (SymptomFactory, EtiologieFactory,
        DiseasePatternFactory, TherapyFactory)

register(SymptomFactory)
register(EtiologieFactory)
register(DiseasePatternFactory)
register(TherapyFactory)
