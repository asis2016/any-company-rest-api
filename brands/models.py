import uuid
from django.conf import settings
from django.contrib.auth import get_user_model

from core.models import TimeStampedModel
from django.db import models


class Brand(TimeStampedModel):
    """
    The Brand model.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    image_url = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.title
