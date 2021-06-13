from rest_framework import serializers

from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    """
    Serializes Testimonial model.
    """

    class Meta:
        fields = ('id', 'client_name', 'client_position', 'image_url', 'testimonial', 'created', 'modified',)
        model = Testimonial
