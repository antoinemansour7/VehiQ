from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import CreateUserAPIView
from accounts.models import Reservation

from django.contrib import admin
from accounts import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', views.AllProfiles)
router.register('reservations', views.AllReservations)

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
    path('user_reservations/', views.user_reservations, name='user_reservations'),
    path('make_reservation/<int:car_id>/', views.make_reservation, name='make_reservation'),
    path('user_reservations/modify/<int:reservation_id>/', views.modify_or_delete_reservation, name='modify_reservation'),
    path('create_user/', CreateUserAPIView.as_view(), name='create_user'),
    path('accounts/login/', views.login_view, name='login'),
     path('', include(router.urls)),
]








