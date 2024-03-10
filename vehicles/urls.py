from django.urls import path
from .views import view_available_vehicles

urlpatterns = [
    path('browse/', view_available_vehicles, name='view_available_vehicles'),
]