from .models import StudentProfile, AcademicProfile, Units
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from datetime import datetime
import uuid


@receiver(pre_save, sender=StudentProfile)
def generate_student_id_and_age(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace("-", "").upper()[:15]
        
    try:
        if datetime.now().strftime('%Y-%m-%d %H:%M:%S') > instance.created.strftime('%Y-%M-%d %H:%M:%S'):
            stud_dob = str(instance.dob)
            strip_dob = datetime.strptime(stud_dob, '%Y-%M-%d')
            calculate_age = datetime.now() - strip_dob
            convert_age = int(calculate_age.days/365.25)
            instance.age = convert_age
            
        else:
            stud_dob = str(instance.dob)
            strip_dob = datetime.strptime(stud_dob, '%Y-%M-%d')
            calculate_age = datetime.now() - strip_dob
            convert_age = int(calculate_age.days/365.25)
            instance.age = convert_age
    
    except AttributeError:
        return

@receiver(pre_save, sender=AcademicProfile)
def generate_academic_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace("-", "").upper()[:15]

@receiver(pre_save, sender=Units)
def generate_units_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace("-", "").upper()[:15]


@receiver(post_save, sender=User)
def create_personal_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff is False and instance.is_superuser is False:
            StudentProfile.objects.create(student=instance)


@receiver(post_save, sender=StudentProfile)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        AcademicProfile.objects.create(academic=instance)
