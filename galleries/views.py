from rest_framework import generics

from .models import Gallery
from .serializers import GallerySerializer


class GalleryListCreate(generics.ListCreateAPIView):
    """
    Lists a Gallery or Creates a Gallery model instance.
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class GalleryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves (gives detail), updates or destroys a Gallery model instance.
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
