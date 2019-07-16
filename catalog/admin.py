from django.contrib import admin

# Register your models here.
from catalog.models import Patient, Illness, Treatment_record

#admin.site.register(Patient)
#admin.site.register(Illness)
#admin.site.register(Treatment_record)

# Define the admin class
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'personalid', 'date_of_birth')
    list_filter = ('return_date','illness')
    fieldsets = (
        (None, {
            'fields': ('name', 'personalid', 'date_of_birth')
        }),
        (None, {
            'fields': ('return_date', 'illness')
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
    pass

