from django.http import JsonResponse
from .utils import geocode_location, get_nearest_branch as utils_get_nearest_branch
from django.views.decorators.http import require_http_methods
import logging


logger = logging.getLogger(__name__)


@require_http_methods(["GET"])  # Restrict this view to only handle GET requests
def get_geocode(request):
    address_or_code = request.GET.get('address')
    if not address_or_code:
        return JsonResponse({'error': 'No address provided'}, status=400)

    try:
        lat, lng = geocode_location(address_or_code)
        if lat is not None and lng is not None:
            return JsonResponse({'latitude': lat, 'longitude': lng})
        else:
            return JsonResponse({'error': 'Geocoding failed'}, status=404)  # Not found status for non-existing addresses
    except Exception as e:
        logger.error(f"Error geocoding address {address_or_code}: {e}")
        return JsonResponse({'error': 'Internal server error'}, status=500)


def get_nearest_branch(request):
    # Wrapper view to call get_nearest_branch from utils
    return utils_get_nearest_branch(request)
