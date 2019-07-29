import datetime

from django import forms


from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from catalog.models import Patient, Illness, Treatment_record, Medication, Severe_illness_record

class MedicalForm(forms.ModelForm):
    class Meta:
        model = Medication

        fields =  ('name', 'duration', 'freq')




class TR_Form(forms.ModelForm):

    class Meta:
        model = Treatment_record
        exclude = ('patient',)
        widgets = {
            
        }
        
     #   fields = '__all__'