from .models import Students, AcademicYear, Units, Assignments, Attendance
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid


@receiver(pre_save, sender=Students)
def generate_studentsID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:20]

@receiver(pre_save, sender=AcademicYear)
def generate_yearID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:20]

@receiver(pre_save, sender=Units)
def generate_unitsID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:20]

@receiver(pre_save, sender=Assignments)
def generate_assignmentsID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:20]

@receiver(pre_save, sender=Attendance)
def generate_attendanceID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:20]
