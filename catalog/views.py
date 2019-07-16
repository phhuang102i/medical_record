from django.shortcuts import render
import datetime

# Create your views here.
from catalog.models import Patient, Illness, Treatment_record

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_patient = Patient.objects.all().count()
    num_illness = Illness.objects.all().count()
    
    # numbers of patient will return this week
    num_patient_thisweek = Patient.objects.filter(name != None)

    
    
    context = {
        'num_patients': num_patient,
        'num_illness': num_illness,
        'num_patient_thisweek': num_patint_thisweek,
		'time': datetime.datetime.now()
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)