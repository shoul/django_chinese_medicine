import factory
from faker import Factory as FakerFactory

faker = FakerFactory.create('de_DE')


class SymptomDetailFactory(factory.django.DjangoModelFactory):
    localisation = 'Head'
    slug = 'foo_symptom'
    indication = 'Pain, stinging'
    description = 'Description for stinging head pain.'

    class Meta:
        model = 'django_chinese_medicine.Symptom'


class SymptomFactory(factory.django.DjangoModelFactory):
    localisation = factory.LazyAttribute(lambda x: faker.name())
    slug = 'foo_symptom'
    indication = factory.LazyAttribute(lambda x: faker.name())
    description = factory.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = 'django_chinese_medicine.Symptom'


class EtiologieFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    slug = 'foo_etiologie'
    description = factory.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = 'django_chinese_medicine.Etiologie'


class DiseasePatternFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    slug = 'foo_disease_pattern'
    manifestation = factory.LazyAttribute(lambda x: faker.text())
    pathologie = factory.LazyAttribute(lambda x: faker.name())

    class Meta:
        model = 'django_chinese_medicine.DiseasePattern'


class TherapyFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    slug = 'foo_therapy'
    intension = factory.LazyAttribute(lambda x: faker.text())
    description = factory.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = 'django_chinese_medicine.Therapy'
