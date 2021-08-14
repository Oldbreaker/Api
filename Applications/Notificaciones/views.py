
from rest_framework.generics import CreateAPIView, ListAPIView
from .serealizers import NotificacionSerializer
from .models import Notificacion


class CrearNotificacion(CreateAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer


class ObtenerNotificacion(ListAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

    def get_queryset(self):
        queryset = Notificacion.objects.all()
        uuid = self.request.query_params.get('UUID', None)
        if uuid is not None:
            queryset = queryset.filter(uuid=uuid)
            return queryset
