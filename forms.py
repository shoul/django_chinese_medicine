from django.forms import ModelForm, BooleanField, CharField, SlugField
from django.core.validators import validate_slug

from .models import Symptom

class FilterBySymptomsForm(ModelForm):
    active = BooleanField(required=False)

    class Meta:
        model = Symptom
        fields = ('active', 'spot', 'result', 'slug')
