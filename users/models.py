from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser




class UserProfile(AbstractUser):
    User_CHOICES = [
        ('In', 'Incharge'),
        ('St', 'Student'),
    ]
    user_type = models.CharField(
        max_length=2,
        choices=User_CHOICES,
        default='Pt',)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    id_photo = models.ImageField(upload_to='media/', blank=True, null=True)
    contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)


