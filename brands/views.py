from rest_framework import generics, permissions

from .models import Brand
from .permissions import IsAuthorOrReadOnly
from .serializers import BrandSerializer

class BrandListCreateAPIView(generics.ListCreateAPIView):
    """
    Lists a Brand or creates a Brand instance.
    """
    # todo LoginRequiredMixins
    #permission_classes=(permissions.IsAuthenticated,)
    #permission_classes = (IsAuthorOrReadOnly,)
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates, or destroys a Brand model instance.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
