import re
from django.urls import re_path

from .consumers import ChatConsumer

websockets_urlpatterns = {
    #expressão regular para a sala ter sempre o mesmo nome
    #ws = websocket
    re_path(r'ws/chat/(?P<nome_sala>\w+)/$', ChatConsumer.as_asgi()),
}
