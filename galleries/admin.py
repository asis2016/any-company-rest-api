from django.contrib import admin

from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    """ Gallery admin. """
    list_display = ('id', 'title', 'created', 'modified',)


admin.site.register(Gallery, GalleryAdmin)
