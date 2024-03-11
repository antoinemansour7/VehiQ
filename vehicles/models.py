from django.db import models

# Create your models here.
    
class Car(models.Model):
    make = models.CharField(max_length=50, default='unknown')
    model = models.CharField(max_length=50, default='unknown')
    year = models.PositiveIntegerField(default=0000)
    price = models.PositiveIntegerField(default=0)
    reserved = models.BooleanField(default=False)
    image = models.ImageField(upload_to='car_images/', default='car_images/default.jpg')
    mileage = models.PositiveIntegerField(default=0)
    company_uuid = models.UUIDField(null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price} - Mileage: {self.mileage} miles"
