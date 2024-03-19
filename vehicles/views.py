from django.shortcuts import get_object_or_404, redirect, render
from vehicles.forms import AddCarForm, EditCarForm
from django.contrib.auth.decorators import login_required
from .models import Car


from rest_framework.response import Response

from .models import Car
from .serializer import CarSerializer

from rest_framework import viewsets




class AvailableVehicles(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    



    
