from django.shortcuts import get_object_or_404, redirect, render
from vehicles.forms import AddCarForm, EditCarForm
from django.contrib.auth.decorators import login_required
from .models import Car

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Car
from .serializer import CarSerializer




class AvailableVehicles(APIView):
    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    

    
