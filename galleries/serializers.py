from rest_framework import serializers

from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    """ Serializers the Gallery model. """

    class Meta:
        fields = ('id', 'title', 'image_url', 'caption', 'created', 'modified',)
        model = Gallery
