from .models import Students, AcademicYear, Units, Assignments, Hostels
from django.core.validators import FileExtensionValidator
from django import forms


class StudentsRegistrationForm(forms.ModelForm):
    """
        New students - students admitted to the institution for the first time - use this form for admission registration.
        The form allows them to select their course, school, degree level, study method in addition to uploading required
        scanned documents, i.e. KCSE result slip, Secondary school leaving and birth certificates.
    """
    SELECT_CATEGORY = (
        (None, '-- Select category --'),
        ('GSSP', 'Government Sponsorship (Bursary, HELB)'),
        ('PSSP', 'Private Sponsorship'),
    )
    SELECT_LEVEL = (
        (None, '-- Select level --'),
        ('Certificate', 'Certificate'),
        ('Diploma', 'Diploma'),
        ('Undergraduate', 'Undergraduate (Bachelors)'),
        ('Post-graduate', 'Post-graduate (Masters)'),
    )
    SELECT_SCHOOL = (
        (None, '-- Select your school --'),
        ('School of Arts, Social Sciences and Business', 'School of Arts, Social Sciences and Business (SASSB)'),
        ('School of Education', 'School of Education (SE)'),
        ('School of Information, Communication & Media Studies', 'School of Information, Communication & Media Studies (INFOCOMS)'),
        ('School of Science, Agriculture & Environmental Science', 'School of Science, Agriculture & Environmental Science (SSAES)'),
    )
    SELECT_STUDY_METHOD = (
        (None, '-- Select study method --'),
        ('Regular', 'Regular'),

    )

    programme = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter your course ...'}),
        label='Course',
    )
    level = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_LEVEL,
    )
    school = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_SCHOOL,
    )
    reg_no = forms.ChoiceField(
        widget=forms.TextInput(attrs={'type': 'text', 'minlength': '12', 'maxlength': '12', 'placeholder': 'Enter your Reg. No.'}),
        help_text='Enter the registration number provided in your admission letter',
    )
    category = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_CATEGORY,
    )
    study_method = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_STUDY_METHOD,
    )
    docs = forms.FileField(
        widget=forms.FileInput(attrs={'type': 'file', 'placeholder': 'attach birth cert., KCSE result slip and your Secondary School leaving cert.', 'class': 'form-control', 'multiple': True}),
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'pdf'])],
        help_text='Upload .jpg, .jpeg or .pdf files only!'
    )

    class Meta:
        model = Students
        fields = ['programme', 'level', 'school', 'reg_no', 'category', 'study_method', 'docs']

class AcademicRegistrationForm(forms.ModelForm):
    """
        Continuing students use this form to facilitate admission registration for each academic year.
    """
    SELECT_ACADEMIC_YEAR = (
        (None, '-- Select academic year --'),
        ('2019/2020', '2019/2020'),
        ('2020/2021', '2020/2021'),
        ('2021/2022', '2021/2022'),
        ('2022/2023', '2022/2023'),
    )
    SELECT_YEAR = (
        (None, '-- Select year of study --'),
        ('First Year', 'First Year (Fresher)'),
        ('Second Year', 'Second Year (Sophomore)'),
        ('Third Year', 'Third Year (Junior)'),
        ('Fourth Year', 'Fourth Year (Senior)'),
    )
    SELECT_SEMESTER = (
        (None, '-- Select semester --'),
        ('1', '1'),
        ('2', '2')
    )

    year = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_YEAR,
    )
    semester = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_SEMESTER,
    )
    academic_year = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_ACADEMIC_YEAR,
    )
    has_deffered = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'py-3 text-danger'}),
        help_text='Check this box if you wish to defer your studies as per info. provided in this form.',
    )

    class Meta:
        model = AcademicYear
        fields = '__all__'

class UnitRegistrationForm(forms.ModelForm):
    """
        This form allows students to register their units per semester.
    """

    class Meta:
        model = Units
        fields = '__all__'

class UploadAssignmentsForm(forms.ModelForm):
    """
        This form is used to upload assignment assigned to students by their respective lecturers. The form can only upload
        document of the specified file types.
    """
    document = forms.FileField(
        widget=forms.FileInput(attrs={'type': 'file', 'placeholder': 'Attach your documents here', 'class': 'form-control'}),
        validators=[FileExtensionValidator(['doc', 'docx', 'odp', 'ods', 'odt', 'pdf', 'ppt', 'xlxs'])],
        help_text='Upload ".doc", ".docx", ".odp", ".ods", ".odt", ".pdf", ".ppt" or ".xlsx" files only!'
    )

    class Meta:
        model = Assignments
        fields = '__all__'

class ResidenceRegistrationForm(forms.ModelForm):
    """
        Students living outside the institution are required to submit non-residence forms each semester to the Hostels & catering
        offices or else they will be fined Kshs.10,000/= after that academic year. This form allows students to provide their residential
        details each semester. The records are stored in the database where they can be used for ref. by the concerned department.
        No need to upload or submit a filled non-residence form.
    """
    SELECT_TYPE_RESIDENCE = (
        (None, '-- Select your type of residence --'),
        ('Campus Resident', 'Campus Resident (You reside or want to reside in school hostel)'),
        ('Non-resident', 'Non-resident'),
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter the name of your hostel ...', 'class': 'mb-2'}),
    )
    landlord = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter the name of your landlord ...', 'class': 'mb-2'}),
    )
    caretaker = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter the name of your caretaker ...', 'class': 'mb-2'}),
    )
    
    residence_type = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_TYPE_RESIDENCE,
    )

    class Meta:
        model = Hostels
        fields = '__all__'