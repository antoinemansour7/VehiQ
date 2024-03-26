from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
import pprint

router = SimpleRouter()
router.register(r'branches', views.BranchViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('geocode/', views.get_geocode, name='get_geocode'),
    path('nearest-branch', views.get_nearest_branch, name='get_nearest_branch'),
]

pprint.pprint(router.urls)
