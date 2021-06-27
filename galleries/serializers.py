from rest_framework import serializers

from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    """
    Serializes the Gallery model.
    """

    class Meta:
        fields = ('id', 'title', 'image_url', 'caption', 'created', 'modified','author',)
        model = Gallery
