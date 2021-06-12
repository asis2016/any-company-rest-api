import uuid

from core.models import TimeStampedModel
from django.db import models


class Brand(TimeStampedModel):
    """
    The Brand model.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    image_url = models.TextField()

    def __str__(self):
        return self.title
