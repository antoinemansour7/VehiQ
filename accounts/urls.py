from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import register_user, login_user, logout_user
from accounts.models import Reservation

from django.contrib import admin
from accounts import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.AllUsers)
router.register('reservations', views.AllReservations)
router.register('user-reservations', views.UserReservationsViewSet, basename='user-reservations')

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('register/', views.register, name='register'),
    # path('user_reservations/', views.user_reservations, name='user_reservations'),
    # path('make_reservation/<int:car_id>/', views.make_reservation, name='make_reservation'),
    # path('user_reservations/modify/<int:reservation_id>/', views.modify_or_delete_reservation, name='modify_reservation'),
    
    # path('accounts/login/', views.login_view, name='login'),
     path('', include(router.urls)),
]








