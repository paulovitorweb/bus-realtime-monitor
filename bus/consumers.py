from typing import Optional
from asgiref.sync import sync_to_async
from django.contrib.gis.geos import Point
from django.utils import timezone
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from bus.models import Terminal


class LocationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'terminal',
            self.channel_name
        )
        await self.accept()

    async def receive_json(self, content: dict):
        if content.get('type') == 'location_update':

            bus_id = content.get('bus_id')
            latitude = content.get('latitude')
            longitude = content.get('longitude')

            if not bus_id or not latitude or not longitude:
                raise ValueError('The fields bus_id, latitude and longitude are required')

            await self.channel_layer.group_send(
                'terminal',
                {
                    'type': 'location_update',
                    'latitude': latitude,
                    'longitude': longitude,
                    'bus_id': str(bus_id),
                },
            )
    
    async def location_update(self, event):
        pass


class TerminalConsumer(AsyncJsonWebsocketConsumer):
    groups = ['terminal']
    terminal = None
    is_inside = []

    async def connect(self):
        self.terminal = await sync_to_async(Terminal.objects.first)()
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive_json(self, content):
        pass

    async def location_update(self, event: dict):

        latitude = event['latitude']
        longitude = event['longitude']
        bus_id = event['bus_id']

        point = Point(longitude, latitude, srid=4326)

        time = timezone.now().strftime('%H:%M')

        position_event = await self._get_event_by_position(bus_id, point)

        await self.send_json(
            {
                'latitude': latitude,
                'longitude': longitude,
                'bus_id': bus_id,
                'time': time,
                'event': position_event
            }
        )

    async def _get_event_by_position(self, bus_id: str, point: Point) -> Optional[str]:
        point_is_inside = self.terminal.geofence.contains(point)

        if not point_is_inside and bus_id in self.is_inside:
            self.is_inside.remove(bus_id)
            return 'saiu do terminal'

        if point_is_inside and bus_id not in self.is_inside:
            self.is_inside.append(bus_id)
            return 'entrou no terminal'
        
        return None
