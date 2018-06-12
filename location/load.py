
from .models import Location
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

# 10.9531499 76.95228359999999
lat = 10.9531499
lng = 76.95228359999999
print(lat)
print(lng)
radius = 4
point = Point(lng, lat)    
print(point)
data = Location.objects.filter(location__distance_lt=(point, Distance(km=radius)))
print(data)