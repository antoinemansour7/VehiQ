from django.db import models
from django.contrib.auth.models import User
from vehicles.models import Car
# Assuming the Car model is defined in the same app for simplicity
# class Car(models.Model):
#     make = models.CharField(max_length=100, default='')
#     model = models.CharField(max_length=100, default='')
#     mileage = models.PositiveIntegerField(default=0)
#     year = models.IntegerField(default=0)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
#     image = models.ImageField(upload_to='uploads/', blank=True, null=True)
#     is_electric = models.BooleanField(default=False)
#     is_all_wheel_drive = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.year} {self.make} {self.model}'
class RentalAgreement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    agreement_text = models.TextField()
    signed = models.BooleanField(default=False)
    date_signed = models.DateTimeField(null=True, blank=True)
    
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    deposit_taken = models.BooleanField(default=False)