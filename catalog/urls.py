from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patients/', views.PatientListView.as_view(), name='patients'),
    path('patient/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
    path('patient/create/', views.PatientCreate.as_view(), name='patient_create'),
    path('patient/<int:pk>/update/', views.PatientUpdate.as_view(), name='patient_update'),
    path('patient/<int:pk>/delete/', views.PatientDelete.as_view(), name='patient_delete'),
]