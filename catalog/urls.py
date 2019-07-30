from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patient/', views.PatientListView.as_view(), name='patient'),
    path('patient/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
    path('patient/create/', views.PatientCreate.as_view(), name='patient_create'),
    path('patient/<int:pk>/update/', views.PatientUpdate.as_view(), name='patient_update'),
    path('patient/<int:pk>/delete/', views.PatientDelete.as_view(), name='patient_delete'),
    path('illness/', views.IllnessListView.as_view(), name='illness'),
    path('illness/<int:pk>', views.IllnessDetailView.as_view(), name='illness-detail'),
    path('illness/create/', views.IllnessCreate.as_view(), name='illness_create'),
    path('illness/<int:pk>/update/', views.IllnessUpdate.as_view(), name='illness_update'),
    path('illness/<int:pk>/delete/', views.IllnessDelete.as_view(), name='illness_delete'),
    path('treatment_record/create/<patient_id>', views.Treatment_recordCreate, name='treatment_record_create'),
    path('inspection_report/', views.Inspection_reportListView.as_view(), name='inspection_report'),
    path('inspection_report/create/', views.Inspection_reportCreate.as_view(), name='inspection_report_create'),
    path('inspection_report/<int:pk>/update/', views.Inspection_reportUpdate.as_view(), name='inspection_report_update'),
    path('inspection_report/<int:pk>/delete/', views.Inspection_reportDelete.as_view(), name='inspection_report_delete'),
    path('inspection_report/', views.Inspection_reportListView.as_view(), name='inspection_report'),
    path('inspection_report/<int:pk>', views.Inspection_reportDetailView.as_view(), name='inspection-report-detail'),

]