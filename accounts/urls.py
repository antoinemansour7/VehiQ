from django.urls import path, include
from . import views
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
     path('', include(router.urls)),
]
