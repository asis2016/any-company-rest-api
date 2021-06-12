from django.contrib import admin

from .models import Brand


class BrandAdmin(admin.ModelAdmin):
    """
    Displays Brand on Django administration.
    """
    list_display = ('id', 'title', 'image_url', 'created', 'modified')


admin.site.register(Brand, BrandAdmin)
