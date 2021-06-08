from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """ Serializes the Project model. """

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'content', 'image_url', 'created', 'modified',)
