from rest_framework import serializers

from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    """ Serializers the Gallery model. """

    class Meta:
        model = Gallery
        fields = ('id', 'title', 'image_url', 'caption', 'created', 'modified',)
