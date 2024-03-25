from django.urls import path
from . import views

urlpatterns = [
    path('sign_agreement/<int:agreement_id>/', views.sign_agreement, name='sign_agreement'),
    path('process_deposit/<int:reservation_id>/', views.process_deposit, name='process_deposit'),
]
