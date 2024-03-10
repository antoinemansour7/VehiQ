from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return self.name
    
class Car(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    reserved = models.BooleanField(default = False)