from django.urls import path
from .views import add_car, view_available_vehicles, edit_car, delete_car

urlpatterns = [
    path('browse/', view_available_vehicles, name='view_available_vehicles'),
    path('add_car/', add_car, name='add_car'),
    path('edit_car/<int:car_id>/', edit_car, name='edit_car'),
    path('delete_car/<int:car_id>/', delete_car, name='delete_car'),
]
