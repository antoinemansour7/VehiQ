from django.urls import path, include
from .views import chat_with_rasa

urlpatterns = [
    path('chat/', chat_with_rasa, name='chat_with_rasa'),
]

