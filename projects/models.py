import uuid

from django.db import models
from core.models import TimeStampedModel


class Project(TimeStampedModel):
    """ Project model. """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image_url = models.TextField()

    def __str__(self):
        return self.title
