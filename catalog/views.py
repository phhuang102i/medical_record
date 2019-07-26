from django.shortcuts import render
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.
from catalog.models import Patient, Illness, Treatment_record, Severe_illness_record, Medication, Inspection_report
from catalog.forms import MedicalForm, TR_Form
from django.template.context_processors import csrf

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

class PatientListView(PermissionRequiredMixin,generic.ListView):
    permission_required = 'catalog.doctor'
    model = Patient
    paginate_by = 15
	
	
class PatientDetailView(PermissionRequiredMixin,generic.DetailView):
    permission_required = 'catalog.doctor'
    model = Patient
	
	

from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




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
	

class IllnessListView(PermissionRequiredMixin,generic.ListView):
    permission_required = 'catalog.doctor'
    model = Illness
    paginate_by = 100

	
class IllnessDetailView(PermissionRequiredMixin,generic.DetailView):
    permission_required = 'catalog.doctor'
    model = Illness
	

class IllnessCreate(PermissionRequiredMixin,CreateView):
    permission_required = 'catalog.doctor'
    model = Illness
    fields = '__all__'
    #initial = {}

class IllnessUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'catalog.doctor'
    model = Illness
    fields = '__all__'

class IllnessDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'catalog.doctor'
    model = Illness
    success_url = reverse_lazy('illness')

from django.shortcuts import get_object_or_404
	
#class Treatment_recordCreate(PermissionRequiredMixin,CreateView):
#    permission_required = 'catalog.doctor'
#    model = Treatment_record
#    patient_id = 1
#    def get_initial(self):
#        patient = get_object_or_404(Patient, id = self.kwargs['patient_id'])
#        return {
#            'patient':patient,
#        }
# 
#    fields = '__all__'

from django.http import HttpResponseRedirect
def Treatment_recordCreate(request,patient_id):

    patient = get_object_or_404(Patient, id =patient_id)

    if request.method == "POST":
        medical_form = MedicalForm(request.POST)
        treatment_record_form = TR_Form(request.POST)
        
        if medical_form.is_valid() and treatment_record_form.is_valid():
            #medication and treatment_record instance save
            treatment_record = treatment_record_form.save()
            treatment_record.patient = patient
            treatment_record.save()
            medication = medical_form.save(False)
                
            medication.treatment = treatment_record
            medication.save()
			# update past_illness and create severe_illness_record if needed
            lst = treatment_record.illness.all()

            for illness_record in lst:
               if illness_record.selection == 'severe':
                   record = Severe_illness_record(illness = illness_record, date = treatment_record.date, patient = treatment_record.patient)
                   recordlst =   [k.illness.name for k in Severe_illness_record.objects.filter(patient__name = treatment_record.patient.name)]
                   if record.illness.name not in recordlst:
                       record.save()
                   if illness_record not in patient.past_illness.all():
                       patient.past_illness.add(illness_record)
		
            return HttpResponseRedirect(("/catalog/patient/"+str(patient_id)))
    else:
        medical_form = MedicalForm()
        treatment_record_form = TR_Form()
    args = {}
    args.update(csrf(request))
    args['medical_form'] = medical_form
    args['treatment_record_form'] = treatment_record_form
    
    return render(request, "catalog/treatment_record_form.html",args)
	
class Inspection_reportListView(PermissionRequiredMixin,generic.ListView):
    permission_required = 'catalog.doctor'
    model = Inspection_report
    paginate_by = 15

class Inspection_reportCreate(PermissionRequiredMixin,CreateView):
    permission_required = 'catalog.doctor'
    model = Inspection_report
    fields = '__all__'
    #initial = {}

class Inspection_reportUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'catalog.doctor'
    model = Inspection_report
    fields = '__all__'

class Inspection_reportDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'catalog.doctor'
    model = Inspection_report
    success_url = reverse_lazy('inspection_report')

