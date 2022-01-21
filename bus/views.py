from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from .models import TerminalSerializer, Terminal

class TerminalViewSet(viewsets.ModelViewSet):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer

def index(request):
    return render(request, 'bus/map.html', {
        'OSM_TILE_LAYER': settings.OSM_CONFIG.get('TILE_LAYER'),
        'OSM_ATTRIBUTION': settings.OSM_CONFIG.get('ATTRIBUTION')
    })

def gps(request):
    return render(request, 'bus/gps.html', {})
