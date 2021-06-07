from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    """ Serializes the Service model. """

    class Meta:
        model = Service
        fields = ('id', 'title', 'icon', 'description',)
