from accounts.models import User
from django.db import models


class Students(models.Model):
    """ This database table stores info about students """
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    name = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    programme = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=70, blank=False)
    school = models.CharField(max_length=50, blank=False)
    reg_no = models.CharField(max_length=12, blank=False)
    category = models.CharField(max_length=30, blank=False)
    docs = models.FileField(upload_to='Students-Docs/Admission-Forms/', null=False)
    study_method = models.CharField(max_length=70, blank=False)
    deffered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ['reg_no']
        verbose_name_plural = 'Students'


class AcademicYear(models.Model):
    """ This model stores details relating to academic year of each student """
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    name = models.ForeignKey(Students, on_delete=models.CASCADE, editable=False)
    year = models.CharField(max_length=10, blank=False)
    semester = models.CharField(max_length=1, blank=False)
    academic_year = models.CharField(max_length=9, blank=False)
    has_deffered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.academic_year}'
    
    class Meta:
        ordering = ['name', 'year']
        verbose_name_plural = 'Academic Year Records'
    

class Units(models.Model):
    """ This model stores info about a student's registered units in each academic year."""
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    student = models.ForeignKey(Students, on_delete=models.CASCADE, editable=False)
    year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, editable=False)
    unit_name = models.CharField(max_length=100, blank=False)
    unit_type = models.CharField(max_length=30, blank=False)
    lecturer = models.CharField(max_length=70, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.unit_name}'
    
    class Meta:
        ordering = ['student', '-year']
        verbose_name_plural = 'Registered Units'
    

class Assignments(models.Model):
    """ This model stores uploaded assignments -> document files """
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    name = models.ForeignKey(Students, on_delete=models.CASCADE, editable=False)
    document = models.FileField(upload_to='Students-Docs/Assignments/', null=False)
    unit_name = models.CharField(max_length=70, blank=False)
    submission_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ['name', 'unit_name', '-submission_date']
        verbose_name_plural = 'Assignments'


class Attendance(models.Model):
    """ This model stores attendance records of each student. """
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    student = models.ForeignKey(Students, on_delete=models.CASCADE, editable=False)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE, editable=False)
    lecturer = models.CharField(max_length=100, blank=False)
    venue = models.CharField(max_length=20, blank=False)
    has_attended = models.BooleanField(default=False)
    attendance_date = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student}'
    
    class Meta:
        ordering = ['student', '-attendance_date']
    

class Hostels(models.Model):
    """ This model is used to store hostel records for each student. A ForeignKey is used to keep track of the hostel
        a student has resided in his/her study period in the institution.
    """
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    student = models.ForeignKey(Students, on_delete=models.CASCADE, editable=False)
    year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=30, blank=False)     # name of the hostel
    landlord = models.CharField(max_length=50, blank=False)
    caretaker = models.CharField(max_length=50, blank=False)
    residence_type = models.CharField(max_length=15, blank=False)   # does the student reside in the school or not
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['student', 'name']
        verbose_name_plural = 'Hostel Records'
    