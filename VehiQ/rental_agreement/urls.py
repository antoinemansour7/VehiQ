# rental_agreements/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.review_agreement, name='review_agreement'),
    path('sign/<int:agreement_id>/', views.sign_agreement, name='sign_agreement'),
    path('signed_confirmation/', views.agreement_signed_confirmation, name='agreement_signed_confirmation'),
]
