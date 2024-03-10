# audioproject/routing.py
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from audioapp.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    'wss': URLRouter(websocket_urlpatterns),
})
