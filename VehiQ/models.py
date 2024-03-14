from django.db import models  # noqa: F401
from accounts.models import Profile  # noqa: F401

# class Company(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()


#     def __str__(self):
#         return self.name

# class Car(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     reserved = models.BooleanField(default = False)


# class Reservation(models.Model):
#     car = models.OneToOneField(Car, on_delete=models.CASCADE)
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     reservation_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.profile.user.username} has reserved {self.car} at {self.reservation_date}. "
