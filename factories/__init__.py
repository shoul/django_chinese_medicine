import factory
from faker import Factory as FakerFactory

faker = FakerFactory.create('de_DE')


class ResultFactory(factory.django.DjangoModelFactory):
    spot = factory.LazyAttribute(lambda x: faker.name())
    result = factory.LazyAttribute(lambda x: faker.name())
    description = factory.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = 'django_chinese_medicine.Result'


class EtiologieFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    description = factory.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = 'django_chinese_medicine.Etiologie'
