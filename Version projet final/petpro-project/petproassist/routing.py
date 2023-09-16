from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
import info.routing  
from info.consumers import YourConsumer, MyConsumer 

application = ProtocolTypeRouter({
    # Autres protocoles (HTTP, Websockets, etc.)
    'websocket': URLRouter([
        path('ws/some_path/', YourConsumer.as_asgi()),  # Spécifiez l'URL de la messagerie WebSocket et le consumer approprié
    
    ]),
})
application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(info.routing.websocket_urlpatterns)
        ),
    }
)