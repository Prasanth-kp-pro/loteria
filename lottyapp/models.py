from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
from django.db import models

from django.db import models
from django.core.validators import RegexValidator

class LotteryEntry(models.Model):
    alphanumeric_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9]{10}$',
        message='Invalid Referal Code'
    )

    referral_code = models.CharField(
        max_length=10,
        validators=[alphanumeric_validator],
        
    )
    REFERRAL_AFFILIATIONS = [
    ('a1', 'A1'),
    ('a2', 'A2'),
    ('a3', 'A3'),
    ('a4', 'A4'),
    ('a5', 'A5'),
    ('a6', 'A6'),
    ('a7', 'A7'),
    ('a8', 'A8'),
    ('a9', 'A9'),
    ('a10', 'A10'),
   
]

    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message='Mobile number must be exactly 10 digits.')])
    winning_number = models.CharField(max_length=5, validators=[RegexValidator(r'^\d{5}$', message='Winning number must be exactly 5 digits.')])
    affiliation = models.CharField(max_length=10, choices=REFERRAL_AFFILIATIONS, null=True)
    def __str__(self):
        return f"{self.name} - {self.referral_code}"
  

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you want for your custom user model
    # For example: profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.username
    


    from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=20)
    winnings = models.DecimalField(max_digits=10, decimal_places=2)
