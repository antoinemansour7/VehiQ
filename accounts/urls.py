from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
    path('user_reservations/', views.user_reservations, name='user_reservations'),
    path('make_reservation/<int:car_id>/', views.make_reservation, name='make_reservation'),
    path('user_reservations/modify/<int:reservation_id>/', views.modify_or_delete_reservation, name='modify_reservation'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('company_dashboard/', views.company_dashboard, name='company_dashboard'),
]
