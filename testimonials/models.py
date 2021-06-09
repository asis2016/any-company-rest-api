import uuid

from core.models import TimeStampedModel
from django.db import models


class Testimonial(TimeStampedModel):
    """
    A Testimonial model.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100, blank=True)
    image_url = models.TextField()
    testimonial = models.TextField(blank=True)

    def __str__(self):
        return self.client_name
