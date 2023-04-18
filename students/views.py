from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import (
    StudentsRegistrationForm, AcademicRegistrationForm, UnitRegistrationForm, UploadAssignmentsForm, ResidenceRegistrationForm,
    )
from .models import AcademicYear


class NewStudentsRegistrationView(View):
    def get(self, request):

        context ={}
        return render(request, 'students/', context)
    
    def post(self, request):
        form = StudentsRegistrationForm()

        if form.is_valid():
            student = form.save(commit=False)
            student.name = request.user
            student.save()

            messages.success(request, f'{student.name} successfully registered!')
            return redirect('student_admission')

class AcademicRegistrationView(View):
    def get(self, request):

        context = {}
        return render(request, 'students/', context)
    
    def post(self, request):
        form = AcademicRegistrationForm()

        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.name = request.user.students
            new_record.save()

            messages.success(request, f'{new_record.name} successfully registered!')
            return redirect('academic_registration')
    
class UnitRegistrationView(View):
    def get(self, request):

        context = {}
        return render(request, 'students/', context)
    
    def post(self, request):
        latest_acad_year = AcademicYear.objects.filter(name=request.user.students).order_by('-academic_year')[0]
        form = UnitRegistrationForm()

        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.student = request.user.students
            new_record.year = latest_acad_year
            new_record.save()

            messages.success(request, 'Units successfully registered!')
            return redirect('unit_registration')
        
class StudentsResidenceRegistrationView(View):
    def get(self, request):

        context = {}
        return render(request, 'students/', context)

    def post(self, request):
        latest_acad_year = AcademicYear.objects.filter(name=request.user.students).order_by('-academic_year')[0]
        form = ResidenceRegistrationForm()

        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.student = request.user.students
            new_record.year = latest_acad_year
            new_record.save()

            messages.success(request, 'Residence info. successfully saved!')
            return redirect('residence_registration')
    
class AssignmentsView(View):
    def get(self, request):

        context = {}
        return render(request, 'students/', context)
    
    def post(self, request):
        form = UploadAssignmentsForm()

        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.name = request.user.students
            assignment.save()

            messages.success(request, 'Document successfully uploaded & saved!')
            return redirect('assignments')
        