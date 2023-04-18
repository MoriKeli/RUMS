from django.urls import path
from . import views

urlpatterns = [
    path('admissions/', views.NewStudentsRegistrationView.as_view(), name='student_admission'),
    path('registration/academic/', views.AcademicRegistrationView.as_view(), name='academic_registration'),
    path('registration/units/', views.UnitRegistrationView.as_view, name='unit_registration'),
    path('registration/residence/', views.StudentsResidenceRegistrationView.as_view(), name='residence_registration'),
    path('assignment/upload/', views.AssignmentsView.as_view(), name='assignments'),

]