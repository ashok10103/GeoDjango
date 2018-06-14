from django.conf.urls import include,url
from .views import HomePageView ,get_data,search



urlpatterns = [
    url(r'^$',HomePageView.as_view(),name="home"),
    url(r'^data/$',get_data,name="data"),
    url(r'^search/$',search,name="search"),
    
    # url(r'^search/$',HomePageView.as_view(),name="home"),
    # url(r'^searchdata$',search,name="search"),    
]