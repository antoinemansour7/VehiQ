from rest_framework import serializers
from .models import Reservation
from vehicles.models import Car
from accounts.models import CustomUser

from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'car', 'user', 'start_date', 'end_date', 'reservation_date', 'pickup_location', 'dropoff_location','card_number', 'confirmation_number']

    # Optionally, you can add extra fields or customize the serializer behavior here



class UserSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ("id", "user", "phone", "visibility", "email", "first_name", "last_name", "is_staff", "is_active", "date_joined")

    def get_user(self, obj):
        return obj.username if obj else None
    





