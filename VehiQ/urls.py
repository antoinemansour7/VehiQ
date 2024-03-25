from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')), # new
    path('api/v1/', include('djoser.urls.authtoken')), # new
    path('api/v1/', include('vehicles.urls')), # new
    path('vehicles/', include('vehicles.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('branches/', include('branches.urls')),]
