from rest_framework import serializers
from .models import Reservation
from vehicles.models import Car
from accounts.models import CustomUser

class ReservationSerializer(serializers.ModelSerializer):
    car_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ('id',"car_name", "user_name", "start_date", "end_date", "reservation_date")
    
    def get_car_name(self, obj):
        return f"{obj.car.make} {obj.car.model}" if obj.car else None
    
    def get_user_name(self, obj):
        return obj.user.username if obj.user else None


class UserSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ("id", "user", "phone", "visibility", "email", "first_name", "last_name", "is_staff", "is_active", "date_joined")

    def get_user(self, obj):
        return obj.username if obj else None
    





