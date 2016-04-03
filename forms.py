from django.forms import Form, BooleanField, ModelForm
from django.core.validators import validate_slug

from .models import Symptom


class ActivateSymptomForm(ModelForm):
    active = BooleanField(required=False)

    class Meta:
        model = Symptom
        fields = ['active', 'slug', 'spot', 'result', 'description']
