from rest_framework import serializers

from .models import Brand


class BrandSerializer(serializers.ModelSerializer):
    """
    Serializes the Brand model.
    """

    class Meta:
        fields = ('id', 'title', 'image_url', 'created', 'modified','author',)
        model = Brand
