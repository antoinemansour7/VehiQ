from django.contrib.gis.db import models as geomodels


class Branch(geomodels.Model):
    name = geomodels.CharField(max_length=255)
    location = geomodels.PointField()
    address = geomodels.CharField(max_length=255)
    city = geomodels.CharField(max_length=50)
    phone = geomodels.CharField(max_length=20, blank=True)
    email = geomodels.EmailField(blank=True)
    services = geomodels.CharField(max_length=255, blank=True)
    opening_hours = geomodels.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
