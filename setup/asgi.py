import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import bus.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            bus.routing.websocket_urlpatterns
        )
    ),
})