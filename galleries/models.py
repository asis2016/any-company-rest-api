import uuid

from core.models import TimeStampedModel
from django.db import models


class Gallery(TimeStampedModel):
    """ Gallery model. """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100, blank=True)
    image_url = models.TextField()
    caption = models.TextField(blank=True)

    def __str__(self):
        return self.title
