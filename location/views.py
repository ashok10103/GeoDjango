from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import  HttpResponse
from .models import Location
# from django.core.exceptions import *
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

# 10.9531499 76.9522835999999
def search(request):
    if request.method == 'POST':
        lat = request.POST.get('latitude', None)
        lon = request.POST.get('longitude', None)
        rad = request.POST.get('radius', None) 
        # lat = 10.9987351
        # lng = 77.03197840000007
        # radius = 4
        point = Point(lon, lat)    
        data = serialize('geojson',Location.objects.filter(location__distance_lt=(point, Distance(km=rad))))  
    
        return HttpResponse(data,content_type='json')

    return render(request,'index.html')


# def index(request):
#    a_list = [1,2,3,4]
#    print (a_list)
#    return render(request, 'index.html', {'list':a_list})

def get_data(request):
    
    lat = 10.9987351
    lng = 77.03197840000007
    radius = 4
    point = Point(lng, lat)    
    data = serialize('geojson',Location.objects.filter(location__distance_lt=(point, Distance(km=radius))))
    
    # data = serialize('geojson',Location.objects.all())
    return HttpResponse(data,content_type='json')