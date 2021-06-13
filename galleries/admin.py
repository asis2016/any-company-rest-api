from django.contrib import admin

from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    """
    Displays Gallery on Django administration.
    """
    list_display = ('id', 'title', 'created', 'modified',)


admin.site.register(Gallery, GalleryAdmin)
