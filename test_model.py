from django.utils.text import slugify

from faker import Faker
fake = Faker('de_DE')

import pytest

from .models import Result

class TestResultModel():

    @pytest.mark.django_db
    def test_make_result(self):
        RESULT_DATA = {}
        for name in ['foo', 'bar', 'baz']:
            spot = fake.name()
            result = fake.name()
            description = fake.text()
            slug = slugify('%s-%s' % (spot, result))
            RESULT_DATA[name]=(spot, slug, result, description)
            Result.objects.create(
                spot=RESULT_DATA[name][0], 
                slug=RESULT_DATA[name][1], 
                result=RESULT_DATA[name][2], 
                description=RESULT_DATA[name][3])
        results = Result.objects.all()
        assert len(results) == 3

    @pytest.mark.django_db
    def test_create_with_save(save):
        foo = Result(spot=fake.name(), result=fake.name(), description=fake.text)
        #foo.slug = slugify('%s-%s' % (foo.spot, foo.result))
        assert foo.save() == None
