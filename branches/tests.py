from django.test import TestCase
from django.urls import reverse
from .models import Branch
from django.contrib.gis.geos import Point
from branches import utils
from .utils import geocode_location
from unittest import mock

class BranchesTestCase(TestCase):
    def setUp(self):
        # Store the original function
        self.original_geocode_location = utils.geocode_location
        # Replace it with your mock
        utils.geocode_location = lambda x: (37.4224082, -122.0856086)

    def tearDown(self):
        # Restore the original function
        utils.geocode_location = self.original_geocode_location

    def test_geocode_failure(self):
        # Simulate failure by changing the mock return value in this test
        utils.geocode_location = lambda x: (None, None)

        # Define an invalid address
        address = "Invalid Address"
        url = reverse('get_geocode') + f'?address={address}'

        # Make a GET request to the URL
        response = self.client.get(url)

        # Verify the response for a failed geocoding attempt
        self.assertEqual(response.status_code, 400)
        expected_error_response = {'error': 'Geocoding failed'}
        self.assertJSONEqual(str(response.content, encoding='utf8'), expected_error_response)

class GeocodingSuccessTestCase(TestCase):
    @mock.patch('branches.utils.geocode_location')
    def test_geocode_success(self, mock_geocode):
        mock_geocode.return_value = (37.4224082, -122.0856086)
        valid_address = "1600 Amphitheatre Parkway, Mountain View, CA"
        url = reverse('get_geocode') + f'?address={valid_address}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print(str(response.content, encoding='utf8'))  # Debugging output
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'latitude': 37.4225295, 'longitude': -122.084299}
        )
