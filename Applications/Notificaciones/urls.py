from django.urls import path
from . import views

app_name = 'Notificacion_app'

urlpatterns = [
    path('notificacion', views.CrearNotificacion.as_view(),),
    path('obtener/<str:uuid>', views.ObtenerNotificacion.as_view(),)


]
