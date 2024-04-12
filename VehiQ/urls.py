from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from chat_interface.views import chat_with_rasa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')), # new
    path('api/v1/', include('djoser.urls.authtoken')), # new
    path('api/v1/', include('vehicles.urls')), # new
    path('vehicles/', include('vehicles.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('branches/', include('branches.urls')),
    path('api/chat/', include('chat_interface.urls')),]
