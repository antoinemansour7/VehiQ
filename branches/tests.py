from django.test import TestCase
from django.urls import reverse
from .models import Branch
from django.contrib.gis.geos import Point
from unittest.mock import patch
import googlemaps  # noqa : F401


class BranchesTestCase(TestCase):
    def setUp(self):
        # Create a test branch
        Branch.objects.create(
            name="Test Branch",
            location=Point(-73.961452, 40.714224),
            address="1600 Amphitheatre Parkway",
            city="Mountain View",
        )

    @patch('branches.views.geocode_location')
    def test_geocode_branch(self, mock_geocode):
        # Mock the geocode_location function to return specific coordinates
        mock_geocode.return_value = (37.4224082, -122.0856086)

        # The address to geocode
        address = "1600 Amphitheatre Parkway, Mountain View, CA"

        # Get geocode URL
        url = reverse('get_geocode') + '?address=' + address

        # Make the request
        response = self.client.get(url)

        # Check the status code and mock effectiveness
        self.assertEqual(response.status_code, 200)
        mock_geocode.assert_called_once_with(address)

        # Assertions for returned data
        response_data = response.json()
        self.assertEqual(response_data['latitude'], 37.4224082)
        self.assertEqual(response_data['longitude'], -122.0856086)

    @patch('branches.views.geocode_location')
    def test_geocode_failure(self, mock_geocode):
        # Simulate a geocoding failure by returning None
        mock_geocode.return_value = (None, None)

        # Address that fails to geocode
        address = "Invalid Address"

        # Get geocode URL
        url = reverse('get_geocode') + '?address=' + address

        # Make the request
        response = self.client.get(url)

        # Check the status code and mock effectiveness
        self.assertEqual(response.status_code, 400)
        mock_geocode.assert_called_once_with(address)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'error': 'Geocoding failed'}
        )
