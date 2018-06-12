from django.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models as gis_models
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=20)
    location=gis_models.PointField(srid=4326)
    objects = GeoManager()
    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name