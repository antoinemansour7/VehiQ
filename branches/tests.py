from django.test import TestCase
from django.urls import reverse
from .models import Branch
from django.contrib.gis.geos import Point
from branches import utils

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
