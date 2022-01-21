from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/bus/', consumers.LocationConsumer.as_asgi()),
    re_path('ws/map/', consumers.TerminalConsumer.as_asgi()),
]