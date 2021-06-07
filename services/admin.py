from django.contrib import admin

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    """ Service admin for http://127.0.0.1:8000/admin/services """
    list_display = ('id', 'title', 'icon',)


admin.site.register(Service, ServiceAdmin)
