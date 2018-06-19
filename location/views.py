from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import  HttpResponse
from .models import Location
# from django.core.exceptions import *
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.template.context_processors import csrf
# Create your views here.



class HomePageView(TemplateView):
    template_name = 'index.html'

# 10.9531499 76.9522835999999



def get_data(request):
    
        lat = float(request.GET.get('latitude'))
        lng = float(request.GET.get('longitude'))
        radius = int(request.GET.get('radius'))
        # lat = 10.9531499
        # lng = 76.9522835999999
        # radius = 4
        print(lat)
        print(lng)
        print(radius)        
        point = Point(lng, lat)    
        print(point)
        data = serialize('geojson',Location.objects.filter(location__distance_lt=(point, Distance(km=radius))))
        print(data)
    # data = serialize('geojson',Location.objects.all())
        return HttpResponse(data,content_type='json')