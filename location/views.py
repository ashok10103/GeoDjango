from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import  HttpResponse
from .models import Location
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def get_data(request):
    data = serialize('geojson',Location.objects.all())
    return HttpResponse(data,content_type='json')