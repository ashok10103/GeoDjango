from django.conf.urls import include,url
from .views import HomePageView ,get_data



urlpatterns = [
    url(r'^$',HomePageView.as_view(),name="home"),
    url(r'^data/$',get_data,name="data"),
    url(r'^location/$',HomePageView.as_view(),name="home"),
]