from django.contrib.gis.db import models as geomodels


class Branch(geomodels.Model):
    name = geomodels.CharField(max_length=255)
    location = geomodels.PointField()
    address = geomodels.CharField(max_length=255)

    def __str__(self):
        return self.name
