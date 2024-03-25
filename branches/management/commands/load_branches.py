from django.core.management.base import BaseCommand
from branches.models import Branch
from django.contrib.gis.geos import Point

class Command(BaseCommand):
    help = 'Loads branch data from a predefined list'

    def handle(self, *args, **options):
        branches_info = [
            {"name": "Branch 1", "address": "Bd Roméo Vachon Nord (Arrivées), Dorval, QC H4Y 1H1", "city": "Dorval", "location": Point(-73.751350, 45.454899)},
            {"name": "Branch 2", "address": "977 Saint-Catherine St W, Montreal, Quebec H3B 4W3", "city": "Montreal", "location": Point(-73.572273, 45.501080)},
            {"name": "Branch 3", "address": "3819 Av. Calixa-Lavallée, Montréal, QC H2L 3A7", "city": "Montréal", "location": Point(-73.569420, 45.527070)},
            {"name": "Branch 4", "address": "300 Sainte Croix Ave, Montreal, Quebec H4N 3K4", "city": "Montreal", "location": Point(-73.667140, 45.509160)},
        ]

        # Attempt to create each branch, catching exceptions for any that fail
        for branch_info in branches_info:
            try:
                Branch.objects.create(**branch_info)
                self.stdout.write(self.style.SUCCESS(f'Successfully loaded branch data for {branch_info["name"]}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Failed to load branch data for {branch_info["name"]}: {e}'))

