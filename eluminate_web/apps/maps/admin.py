from django.contrib.gis import admin
from maps.models import Location

admin.site.register(Location, admin.OSMGeoAdmin)