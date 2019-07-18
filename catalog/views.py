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
    patient_thisweek_list = Patient.objects.filter(return_date__lt = seven_days_fromnow)	
    num_patient_thisweek = patient_thisweek_list.count()

    
    
    context = {
        'num_patients': num_patient,
        'num_illness': num_illness,
        'num_patient_thisweek': num_patient_thisweek,
		'time': datetime.datetime.now(),
        'this_week_patient': patient_thisweek_list
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
	
from django.views import generic

class PatientListView(generic.ListView):
    model = Patient
    paginate_by = 15
	
	
class PatientDetailView(generic.DetailView):
    model = Patient
	
	

from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.forms import JustAForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

class PatientCreate(PermissionRequiredMixin,CreateView):
    permission_required = 'catalog.doctor'
    model = Patient
    fields = '__all__'
    #initial = {}

class PatientUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'catalog.doctor'
    model = Patient
    fields = '__all__'

class PatientDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'catalog.doctor'
    model = Patient
    success_url = reverse_lazy('patients')

