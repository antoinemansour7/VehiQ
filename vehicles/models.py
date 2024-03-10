
from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images')
    is_electric = models.BooleanField(default=False)
    is_all_wheel_drive = models.BooleanField(default=False)
