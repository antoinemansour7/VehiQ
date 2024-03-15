import googlemaps
from django.conf import settings
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from .models import Branch
from django.http import JsonResponse

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key=settings.GMAPS_API_KEY)


def geocode_location(address_or_code):
    """Converts an address or code to geolocation."""
    try:
        geocode_result = gmaps.geocode(address_or_code)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            return location['lat'], location['lng']
        return None, None
    except Exception as e:
        print(f"Geocoding error: {e}")
        return None, None


def get_nearest_branch(request):
    address_or_code = request.GET.get('address')
    if address_or_code:
        user_lat, user_lng = geocode_location(address_or_code)
        user_location = Point(user_lng, user_lat, srid=4326)
        nearest_branch = Branch.objects.annotate(
            distance=Distance('location', user_location)
        ).order_by('distance').first()
        if nearest_branch:
            return JsonResponse({
                'branch_name': nearest_branch.name,
                'branch_address': nearest_branch.address,
                'branch_city': nearest_branch.city
            })
        else:
            return JsonResponse({'error': 'No nearby branch found'}, status=404)
    return JsonResponse({'error': 'No address provided'}, status=400)
