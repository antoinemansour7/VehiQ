# rental_agreements/models.py
from django.db import models
from django.contrib.auth.models import User

class RentalAgreement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property_details = models.TextField()
    agreement_text = models.TextField()
    signed = models.BooleanField(default=False)
    signature_image = models.ImageField(upload_to='signatures/', blank=True, null=True)
    date_signed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Agreement for {self.user.username}"
