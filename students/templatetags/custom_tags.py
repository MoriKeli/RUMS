from django import template
from students.models import Assignment

register = template.Library()

@register.filter(name='file_extension')
def file_extension(value):
    files = Assignment.objects.filter(file_type=value).all()
    extension = [str(f.file_type)[-4:] for f in files][0]
    
    if value:
        return str(extension)
       
    