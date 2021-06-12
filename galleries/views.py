from rest_framework import generics

from rest_framework import permissions
from .models import Gallery
from .serializers import GallerySerializer


class GalleryListCreateAPIView(generics.ListCreateAPIView):
    """
    Lists a Gallery or creates a Gallery model instance.
    """
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class GalleryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves (gives detail), updates or destroys a Gallery model instance.
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
