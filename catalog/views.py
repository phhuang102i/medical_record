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
    seven_days_fromnow = datetime.date.today()+datetime.timedelta(days = 7)
    num_patient_thisweek = Patient.objects.filter(return_date__lt = seven_days_fromnow).count()	

    
    
    context = {
        'num_patients': num_patient,
        'num_illness': num_illness,
        'num_patient_thisweek': num_patient_thisweek,
		'time': datetime.datetime.now()
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
	
from django.views import generic

class PatientListView(generic.ListView):
    model = Patient
    paginate_by = 15
	
	
class PatientDetailView(generic.DetailView):
    model = Patient