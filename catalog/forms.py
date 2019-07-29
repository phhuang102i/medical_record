import datetime

from django import forms
from searchableselect.widgets import SearchableSelect
from django.forms import modelformset_factory

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from catalog.models import Patient, Illness, Treatment_record, Medication, Severe_illness_record

class MedicalForm(forms.ModelForm):
    class Meta:
        model = Medication

        fields =  ('name', 'duration', 'freq')

MedicationFormSet = modelformset_factory(Medication, form=MedicalForm, extra = 3)

class TR_Form(forms.ModelForm):

    class Meta:
        model = Treatment_record
        exclude = ('patient',)
        widgets = {
            'illness': SearchableSelect(model='Illness', search_field='name', many = True)
        }

     #   fields = '__all__'