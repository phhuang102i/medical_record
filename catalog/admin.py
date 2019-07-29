from django.contrib import admin

# Register your models here.
from catalog.models import Patient, Illness, Treatment_record,Medication,Severe_illness_record

#admin.site.register(Patient)
#admin.site.register(Illness)
#admin.site.register(Treatment_record)

# Define the admin class
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'personalid', 'date_of_birth')
    list_filter = ('return_date','allergy')
    fieldsets = (
        (None, {
            'fields': ('name', 'personalid', 'date_of_birth','height','weight','bloodtype')
        }),
        (None, {
            'fields': ('return_date', 'allergy','past_illness')
        }),
    )

# Register the admin class with the associated model
admin.site.register(Patient, PatientAdmin)

class IllnessAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Illness, IllnessAdmin)


@admin.register(Treatment_record)
class Treatment_record_Admin(admin.ModelAdmin):
    list_display = ('date', 'patient')
	
class MedicationAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Medication, MedicationAdmin)

class Severe_illness_recordAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Severe_illness_record, Severe_illness_recordAdmin)

