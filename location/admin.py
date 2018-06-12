from django.contrib.gis import admin
from .models import Location 
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class LocationAdmin(LeafletGeoAdmin):
    list_display=['name','location']

admin.site.register(Location,LocationAdmin)