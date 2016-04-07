from django.forms import Form, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.core.validators import validate_slug

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Symptom


class ActivateSymptomForm(Form):
    symptom_select = ModelMultipleChoiceField(
        queryset=None,
        widget=CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(ActivateSymptomForm, self).__init__(*args, **kwargs)

        self.fields['symptom_select'].queryset = Symptom.objects.all(
                ).order_by('spot', 'result')

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'symptom_index'
        self.helper.add_input(Submit('submit', 'Filtern'))
