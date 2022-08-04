from .forms import LoginForm, SignUpForm, UpdateStudentProfileForm, UpdateAcademicDetailsForm, EditAcademicProfileForm, EditProfile
from .models import StudentProfile, AcademicProfile, Units
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class UserLogin(LoginView):
    authentication_form = LoginForm
    template_name = 'students/login.html'
    

def create_account_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.is_staff = False
            student.username = student.first_name + ' ' + student.last_name
            student.save()
            
            messages.success(request, 'Account created successfully!')
            return redirect('student_profile')
    
    context = {'signup_form': form}
    return render(request, 'students/signup.html', context)


@login_required(login_url='login')
def homepage_view(request):
    
    context = {}
    return render(request, 'students/homepage.html', context)


@login_required(login_url='login')
def student_profile_view(request):
    updateprof_form = UpdateStudentProfileForm(instance=request.user.studentprofile)
    updatestudent_form = UpdateAcademicDetailsForm(instance=request.user.studentprofile.academicprofile)
    editprofile_form = EditProfile(instance=request.user.studentprofile)
    editacademic_form = EditAcademicProfileForm(instance=request.user.studentprofile.academicprofile)
    
    if request.method == 'POST':
        updateprof_form = UpdateStudentProfileForm(request.POST, request.FILES, instance=request.user.studentprofile)
        updatestudent_form = UpdateAcademicDetailsForm(request.POST, request.FILES, instance=request.user.studentprofile.academicprofile)
        
        editprofile_form = EditProfile(request.POST, request.FILES, instance=request.user.studentprofile)
        editacademic_form = EditAcademicProfileForm(request.POST, instance=request.user.studentprofile.academicprofile)
        
        
        if updateprof_form.is_valid() and updatestudent_form.is_valid():
            updateprof_form.save()
            stud = updatestudent_form.save(commit=False)

            stud.save()
            messages.success(request, 'Your profile has been updated and saved!')
            return redirect('student_profile')
            
        
        elif editprofile_form.is_valid():
            editprofile_form.save()
                
            messages.info(request, 'Profile updated successfully!')
            return redirect('student_profile')
                
        elif editacademic_form.is_valid():
            editacademic_form.save()
                
            messages.info(request, 'Academic info. edited successfully!')
            return redirect('student_profile')

    
    context = {'update_form': updateprof_form, 'academic_form': updatestudent_form, 'editprofile_form': editprofile_form,
        'editacademic_form': editacademic_form,
    
    }
    return render(request, 'students/profile.html', context)


class LogoutUser(LogoutView):
    template_name = 'students/logout.html'