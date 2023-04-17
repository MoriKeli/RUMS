from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import NonStaffSignupForm, StaffSignupForm, StudentsSignupForm, EditProfileForm


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'


class StudentsSignupView(View):
    def get(self, request):

        context = {}
        return render(request, 'accounts/students/signup.html', context)
    
    def post(self, request):
        form = StudentsSignupForm()

        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.is_student = True
            new_student.save()

            messages.success(request, 'Student account successfully created!')
            return redirect('profile')

class StaffSignupView(View):
    def get(self, request):

        context = {}
        return render(request, 'accounts/staff/staff.html', context)
    
    def post(self, request):
        form = StaffSignupForm()

        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.is_student = True
            new_student.save()

            messages.success(request, 'Student account successfully created!')
            return redirect('profile')

class NonStaffSignupView(View):
    def get(self, request):

        context = {}
        return render(request, 'accounts/staff/non-staff.html', context)
    
    def post(self, request):
        form = NonStaffSignupForm()

        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.is_student = True
            new_student.save()

            messages.success(request, 'Student account successfully created!')
            return redirect('profile')

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_superuser is False and user.is_staff is False)
class UsersProfileView(View):
    def get(self, request):

        context = {}
        return render(request, 'accounts/profile.html', context)

    def post(self, request):
        form = EditProfileForm(instance=request.user)

        if form.is_valid():
            form.save()

            messages.info(request, 'Profile successfully updated!')
            return redirect('profile')


class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'