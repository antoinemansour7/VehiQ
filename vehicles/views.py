from .models import Car
from .serializer import CarSerializer
from rest_framework import viewsets


class AvailableVehicles(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

