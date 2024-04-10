from django.test import TestCase
from .models import Car
from rest_framework.test import APITestCase  
from .serializer import CarSerializer

class CarModelTest(TestCase):
    def test_model_creation(self):
        car = Car.objects.create(
            make="Tesla",
            model="Model S",
            year=2023,
            mileage=10000,
            price=80000.00,
            is_checked=True,
            is_electric=True
        )

        self.assertEqual(car.make, "Tesla")
        self.assertEqual(car.model, "Model S")
        self.assertEqual(car.year, 2023)
        self.assertEqual(car.mileage, 10000)
        self.assertEqual(car.price, 80000.00)
        self.assertTrue(car.is_checked)
        self.assertTrue(car.is_electric)


class CarSerializerTest(APITestCase):
    def test_serializer_fields(self):
        serializer = CarSerializer(Car.objects.create(make="Toyota", model="Camry"))
        self.assertEqual(set(serializer.data.keys()), {
            "id", "make", "model", "year", "price", "get_image", "is_checked", "is_electric", "is_all_wheel_drive"
        })

from django.test import Client, TestCase

class AvailableVehiclesTest(TestCase):
    def setUp(self):
        self.client = Client()

        Car.objects.create(make="Honda", model="Civic", year=2019, price=20000.00, mileage=10000, is_checked=True, is_electric=False, is_all_wheel_drive=False)
        Car.objects.create(make="Nissan", model="Altima", year=2020, price=25000.00, mileage=20000, is_checked=True, is_electric=False, is_all_wheel_drive=False)

    def test_get_all_cars(self):
        response = self.client.get("/cars/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)  
        self.assertIn("make", response.json()[0])  
