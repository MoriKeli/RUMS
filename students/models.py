from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class StudentProfile(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False)
    student = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=10, blank=False)
    dob = models.DateField(null=True, blank=False)
    age = models.PositiveIntegerField(default=0)
    phone_no = models.CharField(max_length=10, blank=False)
    residence = models.CharField(max_length=50, blank=False)
    home_address = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=60, blank=False)
    ethnicity = models.CharField(max_length=40, blank=False)
    pic = models.ImageField(upload_to='Student-Dps/', default='default.jpg')
    bio = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.student.username}'
    
    class Meta:
        verbose_name_plural = 'Students'
        ordering = ['student']
        
    def save(self, *args, **kwargs):
        super(StudentProfile, self).save(*args, **kwargs)
        
        profile_pic = Image.open(self.pic.path)
        
        if profile_pic.height > 500 and profile_pic.width > 500:
            output_size = (500, 500)
            profile_pic.thumbnail(output_size)
            profile_pic.save(self.pic.path)
        

class AcademicProfile(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False)
    academic = models.OneToOneField(StudentProfile, on_delete=models.CASCADE, editable=False)
    course = models.CharField(max_length=100, blank=False)
    reg_no = models.CharField(max_length=20, blank=False)
    school = models.CharField(max_length=30, blank=False)
    year = models.CharField(max_length=50, blank=False)
    semester = models.CharField(max_length=10, blank=False)
    hostel = models.CharField(max_length=100)
    certificate = models.ImageField(upload_to='Student-Docs/certs', blank=False, null=True)
    result_slip = models.ImageField(upload_to='Student-Docs/slips', blank=False, null=True)
    letter = models.ImageField(upload_to='Student-Docs/letters', blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.academic.student}'
    
    class Meta:
        verbose_name_plural = 'Academic'
        ordering = ['year', 'semester']
        
    
class Units(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False)
    scholar = models.ForeignKey(AcademicProfile, on_delete=models.CASCADE, editable=False)
    unit = models.CharField(max_length=100, blank=False)
    study_mode = models.CharField(max_length=50, blank=False)
    confirmed = models.BooleanField(default=False, editable=False, blank=False)
    registered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.scholar}'
    
    class Meta:
        verbose_name_plural = 'Student\'s Registered Units'
        ordering = ['scholar']
        
