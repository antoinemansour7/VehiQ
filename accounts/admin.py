from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Reservation
from accounts.models import CustomUser  # Import your CustomUser model

# Define a new UserAdmin
class CustomUserAdmin(BaseUserAdmin):
    search_fields = ('username', 'email')

# Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

# Register CustomUserAdmin for CustomUser model
admin.site.register(CustomUser, CustomUserAdmin)

# Register Reservation model with its respective admin class
@admin.register(Reservation)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'reservation_date')  # Display fields in admin list view
