from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Branch

@admin.register(Branch)
class BranchAdmin(OSMGeoAdmin):
    list_display = ('name', 'location', 'address', 'city')
