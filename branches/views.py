from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Branch
from .serializers import BranchSerializer
from django.http import JsonResponse
from .utils import geocode_location, get_nearest_branch as utils_get_nearest_branch

class BranchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    @action(detail=False, methods=['get'])
    def nearest(self, request):
        latitude = request.query_params.get('lat', None)
        longitude = request.query_params.get('lng', None)
        if latitude and longitude:
            user_location = Point(float(longitude), float(latitude), srid=4326)
            nearest_branch = Branch.objects.annotate(
                distance=Distance('location', user_location)
            ).order_by('distance').first()
            serializer = self.get_serializer(nearest_branch)
            return Response(serializer.data)
        else:
            return Response({'error': 'Latitude and longitude parameters are required.'}, status=400)

@api_view(['GET'])
def get_geocode(request):
    address_or_code = request.GET.get('address', '')
    if address_or_code:
        lat, lng = geocode_location(address_or_code)
        if lat is not None and lng is not None:
            return JsonResponse({'latitude': lat, 'longitude': lng})
        else:
            return JsonResponse({'error': 'Geocoding failed'}, status=400)
    return JsonResponse({'error': 'No address provided'}, status=400)

def get_nearest_branch(request):
    return utils_get_nearest_branch(request)
