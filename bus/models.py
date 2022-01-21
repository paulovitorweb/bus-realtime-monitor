from uuid import uuid4
from django.contrib.gis.db import models as gis_models
from django.db import models
from rest_framework_gis import serializers


class Terminal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=150)
    geofence = gis_models.PolygonField()

    class Meta:
        db_table = 'bus.terminals'

    def __str__(self):
        return self.name


class TerminalSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Terminal
        fields = "__all__"
        geo_field = 'geofence'
