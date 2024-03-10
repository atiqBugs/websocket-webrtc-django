from django.urls import re_path

from .consumers import AudioConsumer

websocket_urlpatterns = [
    re_path(r"wss/audio/(?P<room_name>\w+)/$", AudioConsumer.as_asgi()),
]

