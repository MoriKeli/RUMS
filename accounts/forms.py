from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


SELECT_GENDER = (
    (None, '-- Select your gender --'),
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class StudentsSignupForm(UserCreationForm):
    """ This form is used by students to create an account. """
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autocomplete': True}),
        required=True,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autocomplete': True}),
        required=True,
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autocomplete': True}),
        required=True,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'type': 'email', 'class': 'mb-2'}),
        required=True,
    )
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_GENDER,
    )
    dob = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'mb-2'}),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'dob', 'password1', 'password2']


class StaffSignupForm(UserCreationForm):
    """ This form is used by teaching staff to create an account. """
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autocomplete': True}),
        required=True,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autocomplete': True}),
        required=True,
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autocomplete': True}),
        required=True,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'type': 'email', 'class': 'mb-2'}),
        required=True,
    )
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_GENDER,
    )
    dob = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'mb-2'}),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'dob', 'password1', 'password2']

class NonStaffSignupForm(UserCreationForm):
    """ This sign up form is used by non-teaching staff to create an account """
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autocomplete': True}),
        required=True,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autocomplete': True}),
        required=True,
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autocomplete': True}),
        required=True,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'type': 'email', 'class': 'mb-2'}),
        required=True,
    )
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_GENDER,
    )
    dob = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'mb-2'}),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'dob', 'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    """ This form allow users to update their profile. """
    SELECT_MARITAL_STATUS = (
        (None, '-- Select your marital status --'),
        ('Single', 'Single'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
    )
    SELECT_RELIGION = (
        (None, '-- Select your religion --'),
        ('Budhism', 'Budhism'),
        ('Christianity', 'Christianity'),
        ('Hinduism', 'Hinduism'),
        ('Islam', 'Islam'),
        ('Judaism', 'Judaism'),
        ('Rastafarian', 'Rastafarian'),
        ('Taoism', 'Taoism'),
    )
    SELECT_TITLE = (
        (None, '-- Select title --'),
        ('Mr', 'Mr.'),
        ('Mrs', 'Mrs.'),
        ('Miss', 'Miss'),
        ('Madam', 'Madam'),
    )

    national_id = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'minlength': '8', 'maxlength': '8', 'min': '12306780'}),
        help_text='Enter your national ID. card number', required=False,
    )
    phone_no = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'minlength': 10, 'maxlength': 10, 'placeholder': 'Enter your mobile number'}),
        help_text='Enter your number without your country code'
    )
    marital_status = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_MARITAL_STATUS,
    )
    religion = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_RELIGION,
    )
    title = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_TITLE,
    )

    class Meta:
        model = User
        fields = [
            'national_id', 'phone_no', 'marital_status', 'religion',
            'title', 'profile_pic',
        ]
