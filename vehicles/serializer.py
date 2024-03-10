from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "make", "model", "year", "price", "get_image", "is_electric", "is_all_wheel_drive")
