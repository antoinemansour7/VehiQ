import googlemaps
from django.conf import settings
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from .models import Branch
from django.http import JsonResponse
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)

def get_gmaps_client():
    """Lazy load the Google Maps Client."""
    logger.debug(f"Using API Key: {settings.GMAPS_API_KEY}")
    return googlemaps.Client(key=settings.GMAPS_API_KEY)

def geocode_location(address_or_code):
    print("geocode_location called")
    """Converts an address or code to geolocation with caching."""
    cache_key = f'geocode_{address_or_code}'
    cached_result = cache.get(cache_key)
    if cached_result:
        logger.info(f"Cache hit for: {address_or_code}")
        return cached_result

    gmaps = get_gmaps_client()
    try:
        logger.info(f"Attempting to geocode: {address_or_code}")
        geocode_result = gmaps.geocode(address_or_code)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            lat_lng = (location['lat'], location['lng'])
            cache.set(cache_key, lat_lng, 86400)  # Cache for 24 hours
            return lat_lng
    except Exception as e:
        logger.error(f"Geocoding error: {e}")
    return None, None

def get_nearest_branch(request):
    address_or_code = request.GET.get('address')
    max_distance = request.GET.get('max_distance', 20)  # Optional max distance in kilometers

    if address_or_code:
        user_lat, user_lng = geocode_location(address_or_code)
        if user_lat is None or user_lng is None:
            return JsonResponse({'error': 'Geocoding failed'}, status=400)

        user_location = Point(user_lng, user_lat, srid=4326)
        queryset = Branch.objects.annotate(
            distance=Distance('location', user_location)
        ).order_by('distance')

        if max_distance:
            queryset = queryset.filter(distance__lte=max_distance * 1000)  # Convert km to meters

        branches = list(queryset.values('name', 'address', 'city', 'distance')[:5])  # Limit to 5 results
        if branches:
            return JsonResponse({'branches': branches}, safe=False)
        else:
            return JsonResponse({'error': 'No nearby branch found'}, status=404)
    return JsonResponse({'error': 'No address provided'}, status=400)
