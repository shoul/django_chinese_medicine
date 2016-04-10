import factory
from faker import Factory as FakerFactory

faker = FakerFactory.create('de_DE')


class SymptomDetailFactory(factory.django.DjangoModelFactory):
    localisation = 'Head'
    slug = 'head_pain_stinging'
    indication = 'Pain, stinging'
    description = 'Description for stinging head pain.'

    class Meta:
        model = 'django_chinese_medicine.Symptom'


class SymptomFactory(factory.django.DjangoModelFactory):
    localisation = factory.LazyAttribute(lambda x: faker.name())
    slug = 'foo'
    indication = factory.LazyAttribute(lambda x: faker.name())
    description = factory.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = 'django_chinese_medicine.Symptom'


class EtiologieDetailFactory(factory.django.DjangoModelFactory):
    name = 'Etiologie Foo'
    slug = 'etiologie_foo'
    description = 'Description for Etiologie Foo.'

    class Meta:
        model = 'django_chinese_medicine.Etiologie'


class EtiologieFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    slug = 'foo'
    description = factory.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = 'django_chinese_medicine.Etiologie'


class DiseasePatternDetailFactory(factory.django.DjangoModelFactory):
    name = 'Disease pattern Foo'
    slug = 'disease_pattern_foo'
    manifestation = 'Manifestation Foo'
    pathologie = 'Pathologie Foo'
    # TODO: Add related factory

    class Meta:
        model = 'django_chinese_medicine.DiseasePattern'


class DiseasePatternFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    slug = 'foo'
    manifestation = factory.LazyAttribute(lambda x: faker.text())
    pathologie = factory.LazyAttribute(lambda x: faker.name())

    class Meta:
        model = 'django_chinese_medicine.DiseasePattern'


class TherapyDetailFactory(factory.django.DjangoModelFactory):
    name = 'Therapie Foo'
    slug = 'therapie_foo'
    intension = 'Intension Foo'
    description = 'Description Foo'

    class Meta:
        model = 'django_chinese_medicine.Therapy'


class TherapyFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    slug = 'foo'
    intension = factory.LazyAttribute(lambda x: faker.text())
    description = factory.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = 'django_chinese_medicine.Therapy'
