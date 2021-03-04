from django.contrib import admin
from .models import LogRequest


class LogRequestAdmin(admin.ModelAdmin):
    fields = ['service', 'consumer', 'proxy', 'gateway', 'request', 'line', 'started_at']


admin.site.register(LogRequest, LogRequestAdmin)
