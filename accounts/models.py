from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Profile(models.Model):
    VISIBILITY_CHOICES = (
        ('public', 'Public'), 
        ('private', 'Private'), 
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Example additional fields
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    visibility = models.CharField(max_length=7, choices=VISIBILITY_CHOICES, default='public')

    def __str__(self):
        return self.user.username

    def profile_completion_status(self): 
        fields_filled = sum(bool(getattr(self, field.name)) for field in self._meta.fields)
        total_fields = len(self._meta.fields)
        completion_percentage = int((fields_filled / total_fields) * 100)
        return completion_percentage


