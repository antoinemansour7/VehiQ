from django.urls import path
from . import views

urlpatterns = [
    path('geocode/', views.get_geocode, name='get_geocode'),
    path('nearest-branch', views.get_nearest_branch, name='get_nearest_branch'),
]
