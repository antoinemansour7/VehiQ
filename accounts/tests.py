# from django.test import TestCase
# from django.contrib.auth.models import User
 
# from django.db.models.signals import post_save  # noqa: F401
# from django.dispatch import receiver  # noqa: F401
# from django.urls import reverse


# class ProfileModelTests(TestCase):

#     def setUp(self):
#         # Create a user instance, which should trigger profile creation
#         self.user = User.objects.create_user(username='testuser', password='testpassword')

#     def test_profile_creation(self):
#         """
#         Test that a Profile instance is created when a new User is saved.
#         """
#         self.assertTrue(Profile.objects.filter(user=self.user).exists(), "Profile was not created for new user.")

#     def test_profile_link_to_user(self):
#         """
#         Test that the created Profile instance is correctly linked to the User instance.
#         """
#         user_profile = Profile.objects.get(user=self.user)
#         self.assertEqual(self.user.profile, user_profile, "User's profile is not linked correctly.")

#     def test_delete_user_cascades_to_profile(self):
#         """
#         Test that deleting a User instance also deletes the associated Profile instance.
#         """
#         user_id = self.user.id
#         self.user.delete()
#         self.assertFalse(Profile.objects.filter(user_id=user_id).exists(), "Profile was not deleted when the User was deleted.")


# class ProfileFormTests(TestCase):

#     def test_phone_field_validation(self):
#         form_data = {'bio': 'Test Bio', 'phone': '+1234567890'}
#         form = ProfileForm(data=form_data)
#         self.assertTrue(form.is_valid())

#     def test_invalid_phone_field_validation(self):
#         form_data = {'bio': 'Test Bio', 'phone': 'invalidphone'}
#         form = ProfileForm(data=form_data)
#         self.assertFalse(form.is_valid())


# class ProfileViewTests(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='testviewuser', password='password')
#         self.client.login(username='testviewuser', password='password')

#     def test_edit_profile_view(self):
#         response = self.client.get(reverse('accounts:edit_profile'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'form')



# accounts/tests.py
from django.test import TestCase
from django.utils import timezone
from .models import CustomUser, Reservation
from vehicles.models import Car  
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import register_user, login_user, logout_user, AllUsers
from django.test import TestCase
from accounts.models import CustomUser
from accounts.serializers import UserSerializer
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from accounts.models import Reservation, CustomUser
from accounts.serializers import ReservationSerializer


class CustomUserModelTest(TestCase):
    def test_user_creation(self):
        user = CustomUser.objects.create_user(username='testuser', email='user@test.com', phone='1234567890', visibility='public')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'user@test.com')
        self.assertEqual(user.phone, '1234567890')
        self.assertEqual(user.visibility, 'public')

class ReservationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = CustomUser.objects.create_user(username='testuser', email='user@test.com')
        cls.car = Car.objects.create(brand='Test Brand', model='Test Model', year='2020')  # Adapt these fields based on your Car model
        cls.reservation = Reservation.objects.create(
            car=cls.car,
            user=cls.user,
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=1),
            pickup_location='Test Pickup',
            dropoff_location='Test Dropoff',
            card_number='1234567890123456',
            confirmation_number='1234567890',
            price='100.00',
            deposit='50.00'
        )

    def test_reservation_str(self):
        self.assertEqual(str(self.reservation), f"{self.user.username} has reserved {self.car} at {self.reservation.reservation_date}. ")

    def test_is_modification_allowed(self):
        # This test assumes you add a `modification_allowed_until` DateTimeField to your Reservation model
        future_time = timezone.now() + timezone.timedelta(hours=1)
        self.reservation.modification_allowed_until = future_time
        self.assertTrue(self.reservation.is_modification_allowed())
        # Test for a past time
        past_time = timezone.now() - timezone.timedelta(hours=1)
        self.reservation.modification_allowed_until = past_time
        self.assertFalse(self.reservation.is_modification_allowed())




class TestUrls(SimpleTestCase):
    
    def test_register_url_resolves(self):
        url = reverse('accounts:register')
        self.assertEquals(resolve(url).func, register_user)

    def test_login_url_resolves(self):
        url = reverse('accounts:login')
        self.assertEquals(resolve(url).func, login_user)

    def test_logout_url_resolves(self):
        url = reverse('accounts:logout')
        self.assertEquals(resolve(url).func, logout_user)

    def test_all_users_url_resolves(self):
        url = reverse('accounts:user-list')  # Assuming 'user-list' is the automatically generated name for the list route of the AllUsers viewset
        self.assertEquals(resolve(url).func.__name__, AllUsers.as_view(actions={'get': 'list'}).__name__)


class UserRegistrationTest(APITestCase):
    def test_user_registration_success(self):
        url = reverse('register_user')  # Use the correct name you've assigned in urls.py
        data = {
            'username': 'testuser',
            'password': 'securepassword',
            'email': 'testuser@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.get().username, 'testuser')

    def test_user_registration_fail(self):
        # Assuming you want to test failure due to missing fields
        url = reverse('register_user')  # Use the correct name you've assigned in urls.py
        data = {}  # Empty data should fail due to missing fields
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)






class UserLoginTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user to test login
        cls.user = get_user_model().objects.create_user(username='loginuser', email='loginuser@example.com', password='testpass123')

    def test_user_login_success(self):
        url = reverse('login_user')  # Use the correct name you've assigned in urls.py
        data = {
            'email': 'loginuser@example.com',
            'password': 'testpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('isLoggedIn', response.json())

    def test_user_login_fail(self):
        url = reverse('login_user')  # Use the correct name you've assigned in urls.py
        data = {
            'email': 'loginuser@example.com',
            'password': 'wrongpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a CustomUser instance to use in tests
        cls.user = CustomUser.objects.create(
            username='testuser',
            email='test@example.com',
            phone='1234567890',
            visibility='public',
            first_name='Test',
            last_name='User',
            is_staff=False,
            is_active=True
        )

    def test_user_serializer(self):
        # Serialize the user instance
        serializer = UserSerializer(instance=self.user)
        
        # Check if the serialized data matches expected values
        expected_data = {
            'id': self.user.id,
            'user': self.user.username,
            'phone': '1234567890',
            'visibility': 'public',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'is_staff': False,
            'is_active': True,
            'date_joined': self.user.date_joined.isoformat()  # Formatting date for comparison
        }
        self.assertEqual(serializer.data, expected_data)



class ReservationSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Assuming a Car model exists and has been imported
        cls.car = Car.objects.create(make='Test Make', model='Test Model')
        cls.user = CustomUser.objects.create(username='reservuser', email='reserv@example.com')
        cls.reservation = Reservation.objects.create(
            car=cls.car,
            user=cls.user,
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=1),
            reservation_date=timezone.now(),
            pickup_location='Test Pickup',
            dropoff_location='Test Dropoff',
            card_number='1234123412341234',
            confirmation_number='CONF12345',
            price='100.00',
            deposit='20.00'
        )

    def test_reservation_serializer(self):
        serializer = ReservationSerializer(instance=self.reservation)
        
        # Simplified check focusing on a few fields
        self.assertEqual(serializer.data['user'], self.user.id)
        self.assertEqual(serializer.data['car'], self.car.id)  # Assuming Car model's id field
        self.assertEqual(serializer.data['pickup_location'], 'Test Pickup')