from io import BytesIO
from PIL import Image
from django.db import models


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100, default='')
    model = models.CharField(max_length=100, default='')
    mileage = models.PositiveIntegerField(default=0)
    year = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    is_checked = models.BooleanField(default=False)
    is_electric = models.BooleanField(default=False)
    is_all_wheel_drive = models.BooleanField(default=False)
    
    def __str__(self):  # Fixed typo here
        return f'{self.year} {self.make} {self.model}'
    
    def get_image(self):
        if self.image:
             return 'http://127.0.0.1:8000'+self.image.url  # Added the port number in the URL
        return ''


