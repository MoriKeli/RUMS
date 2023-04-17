from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class User(AbstractUser):
    """ This is the main User model. """
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=7, blank=False)
    dob = models.DateField(null=True, blank=False)
    age = models.PositiveIntegerField(default=0, editable=False)
    phone_no = models.CharField(max_length=10, blank=False)
    national_id = models.CharField(max_length=8, blank=False)
    marital_status = models.CharField(max_length=10, blank=False)
    religion = models.CharField(max_length=10, blank=False)
    title = models.CharField(max_length=5, blank=False)
    profile_pic = models.ImageField(upload_to='User-dps/', default='default.jpg')
    is_student = models.BooleanField(default=False)
    is_teachingstaff = models.BooleanField(default=False)
    is_classrep = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.username}'
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
    
        img = Image.open(self.profile_pic.path)     # find path of the uploaded image. Note: the image is not saved in the db.

        if img.height > 400 and img.width > 400:    # check if its greater than 400x400 pixels
            output_size = (400, 400)
            img.thumbnail(output_size)  # resize it according to the values of the output_size
            img.save(self.profile_pic.path)  # save it in db
    
    class Meta:
        ordering = ['username']
        