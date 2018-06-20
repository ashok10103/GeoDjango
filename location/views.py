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





def get_data(request):    
    lat = float(request.GET.get('latitude'))
    lng = float(request.GET.get('longitude'))
    radius = int(request.GET.get('radius'))      
    point = Point(lng, lat)      
    data = serialize('geojson',Location.objects.filter(location__distance_lt=(point, Distance(km=radius))))    
    # data = serialize('geojson',Location.objects.all())
    return HttpResponse(data,content_type='json')