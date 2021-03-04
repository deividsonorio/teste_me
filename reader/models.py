from django.db import models


class LogRequest(models.Model):
    service = models.CharField("Service ID", max_length=50)
    consumer = models.CharField("Consumer ID", max_length=50)
    proxy = models.IntegerField("Proxy", default=0)
    gateway = models.IntegerField("Gateway", default=0)
    request = models.IntegerField("Request", default=0)
    line = models.TextField("Original Log Line")
    started_at = models.CharField("Started At", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
