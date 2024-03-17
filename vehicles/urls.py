from django.urls import path, include
from django.contrib import admin
from vehicles import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cars', views.AvailableVehicles)

urlpatterns = [
    path('', include(router.urls)),
   
]

