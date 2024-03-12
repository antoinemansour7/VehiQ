from rest_framework import serializers
from .models import Reservation
from vehicles.models import Car
from .models import Profile

class ReservationSerializer(serializers.ModelSerializer):
    car_name = serializers.SerializerMethodField()
    profile_name=serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ("car_name", "profile_name", "start_date", "end_date", "reservation_date")
    
    def get_car_name(self, obj):
        return obj.car.make+" "+obj.car.model if obj.car else None
    
    def get_profile_name(self, obj):
        return obj.profile.user.username if obj.profile else None
    



