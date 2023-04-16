from .models import StudentProfile, AcademicProfile, Units, Assignment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.fields['username'].label = 'Name'

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True, label='Surname')
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        
class UpdateStudentProfileForm(forms.ModelForm):
    CHOICE_GENDER = (
        (None, '-- Select your gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), label='', choices=CHOICE_GENDER)
    dob = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mt-2'}), label='', help_text='Enter your date of birth')
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mt-2', 'placeholder': 'Enter your phone no. ...'}), label='')
    residence = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mt-2', 'placeholder': 'Enter your hometown ...'}), label='')
    home_address = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mt-2', 'placeholder': 'Enter P.O. Box'}), label='')
    country = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mt-2', 'placeholder': 'Enter your country of origin ...'}), label='')
    ethnicity = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mt-2', 'placeholder': 'Enter your ethnicity ...'}), label='')
    pic = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'mt-2'}), label='', help_text='Upload your image.')
    
    class Meta:
        model = StudentProfile
        exclude = ['age', 'bio']
        
class UpdateAcademicDetailsForm(forms.ModelForm):
    CHOICE_SCHOOL = (
        (None, '-- Select one option --'),
        ('INFOCOMS', 'INFOCOMS'),
        ('SANRES', 'SANRES'),
        ('SSTE', 'SSTE'),
    )
    CHOICE_YEAR = (
        (None, '-- Select year of study --'),
        ('1st year', '1st year'),
        ('2nd year', '2nd year'),
        ('3rd year', '3rd year'),
        ('4th year', '4th year'),
    )
    CHOICE_SEMESTER = (
        (None, 'Select semester'),
        ('1', '1'),
        ('2', '2'),
    )
    course = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter the course your are studying'}), label='')
    reg_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter Registration No.', 'class': 'mt-2'}), label='')
    school = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2'}), choices=CHOICE_SCHOOL, label='')
    year = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2'}), choices=CHOICE_YEAR, label='')
    semester = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2'}), choices=CHOICE_SEMESTER, label='')
    hostel = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter name of your hostel', 'class': 'mt-2'}), label='', required=False)
    certificate = forms.ImageField(widget=forms.FileInput(attrs={'type':'file', 'class': 'mt-2'}), label='', required=True, help_text='Upload Secondary sch. leaving certificate')
    result_slip = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file'}), label='', required=True, help_text='Upload result slip/KCSE Certificate')
    letter = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file'}), label='', required=True, help_text='Upload admission letter')
    
    class Meta:
        model = AcademicProfile
        fields = ['course', 'reg_no', 'school', 'year', 'semester', 'hostel', 'certificate', 'result_slip', 'letter']
        

class EditProfile(forms.ModelForm):
    pic = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'mt-2'}), label='', help_text='Upload your image.')
    
    class Meta:
        model = StudentProfile
        fields = ['pic']
        
        
class EditAcademicProfileForm(forms.ModelForm):
    CHOICE_YEAR = (
        (None, '-- Select year of study --'),
        ('1st year', '1st year'),
        ('2nd year', '2nd year'),
        ('3rd year', '3rd year'),
        ('4th year', '4th year'),
    )
    CHOICE_SEMESTER = (
        (None, '-- Select semester --'),
        ('1', '1'),
        ('2', '2'),
    )
    year = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2'}), choices=CHOICE_YEAR, label='')
    semester = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2'}), choices=CHOICE_SEMESTER, label='')
    hostel = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter your hostel', 'class': 'mt-2'}), label='', required=False)
    
    class Meta:
        model = AcademicProfile
        fields = ['year', 'semester', 'hostel']


class UnitRegistrationForm(forms.ModelForm):
    CHOICE_STUDY = (
        (None, '-- Select study mode --'),
        ('Online', 'Online'),
        ('Regular', 'Regular'),
    )
    CHOICE_UNITS = (
        (None, '-- Register your units --'),
        ('Unit 1', 'Unit 1'),
        ('Unit 2', 'Unit 2'),
        ('Unit 3', 'Unit 3'),
        ('Unit 4', 'Unit 4'),
        ('Unit 5', 'Unit 5'),
        ('Unit 6', 'Unit 6'),
    )
    study_mode = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2 mb-2'}), label='', required=True, choices=CHOICE_STUDY)
    unit = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), label='', required=True, choices=CHOICE_UNITS)
    
    class Meta:
        model = Units
        fields = ['study_mode', 'unit']
        

class UploadAssignmentForm(forms.ModelForm):
    CHOICE_UNITS = (
        (None, '-- Register your units --'),
        ('Unit 1', 'Unit 1'),
        ('Unit 2', 'Unit 2'),
        ('Unit 3', 'Unit 3'),
        ('Unit 4', 'Unit 4'),
        ('Unit 5', 'Unit 5'),
        ('Unit 6', 'Unit 6'),
    )
    unit = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2'}), label='', required=True, choices=CHOICE_UNITS)
    file_type = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'mb-2'}), label='', required=True, validators=[FileExtensionValidator(['doc', 'docx', 'odt', 'pdf', 'ppt', 'xlsx'])])
    
    class Meta:
        model = Assignment
        fields = ['file_type', 'unit']
    