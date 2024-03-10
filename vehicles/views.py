from django.shortcuts import render

from vehicles.models import Car

def view_available_vehicles(request):
    available_vehicles = Car.objects.filter(reserved=False)  # Query for available cars
    return render(request, 'vehicles/view_available_vehicles.html', {'available_vehicles': available_vehicles})