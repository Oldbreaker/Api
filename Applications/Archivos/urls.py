from django.urls import path
from . import views

app_name = 'Archivo_app'

urlpatterns = [
    path('File', views.File.as_view(),
         )

]
