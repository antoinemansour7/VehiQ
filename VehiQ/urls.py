
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')), # new
    path('api/v1/', include('djoser.urls.authtoken')), # new


    path('vehicles/', include('vehicles.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
