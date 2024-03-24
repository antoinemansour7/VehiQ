
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete  # noqa: F401
from django.dispatch import receiver  # noqa: F401
from vehicles.models import Car

class CustomUser(AbstractUser):
    VISIBILITY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
        ('csr', 'CSR'),
    )

    phone = models.CharField(max_length=10, blank=True, null=True)
    visibility = models.CharField(max_length=7, choices=VISIBILITY_CHOICES, default='public')

    def __str__(self):
        return self.username



class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use CustomUser instead of Profile
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    reservation_date = models.DateTimeField(default=timezone.now)
    pickup_location = models.CharField(max_length=100,default='')  
    dropoff_location = models.CharField(max_length=100,default='')
    card_number = models.CharField(max_length=16, default='')
    confirmation_number = models.CharField(max_length=10, default='')

    def __str__(self):
        return f"{self.user.username} has reserved {self.car} at {self.reservation_date}. "

    def is_modification_allowed(self):
        return timezone.now <= self.modification_allowed_until
