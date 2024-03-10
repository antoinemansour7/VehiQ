from django.urls import path, include

from vehicles import views

urlpatterns = [
    path('browse/', views.AvailableVehicles.as_view()),
]
