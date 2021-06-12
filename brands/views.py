from rest_framework import generics

from .models import Brand
from .serializers import BrandSerializer


class BrandListCreateAPIView(generics.ListCreateAPIView):
    """
    Lists a Brand or creates a Brand instance.
    """
    # todo LoginRequiredMixins
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates, or destroys a Brand model instance.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
