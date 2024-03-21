import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete  # noqa: F401
from django.dispatch import receiver  # noqa: F401
from vehicles.models import Car


class Profile(models.Model):
    VISIBILITY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    visibility = models.CharField(max_length=7, choices=VISIBILITY_CHOICES, default='public')

    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.username

    def profile_completion_status(self):
        fields_filled = sum(bool(getattr(self, field.name)) for field in self._meta.fields)
        total_fields = len(self._meta.fields)
        completion_percentage = int((fields_filled / total_fields) * 100)
        return completion_percentage


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    modification_allowed_until = models.DateTimeField()
    reservation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.profile.user.username} has reserved {self.car} at {self.reservation_date}. "

    def is_modification_allowed(self):
        return timezone.now <= self.modification_allowed_until
