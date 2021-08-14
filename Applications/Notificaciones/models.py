from django.utils import timezone
from django.db import models


class Notificacion(models.Model):
    date = models.DateTimeField(default=timezone.now)
    UUID = models.UUIDField()
    event_type = models.CharField(max_length=50)
    event_data = models.JSONField()
