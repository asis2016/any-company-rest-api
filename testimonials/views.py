from rest_framework import generics

from .models import Testimonial
from .serializers import TestimonialSerializer


class TestimonialListCreate(generics.ListCreateAPIView):
    """
    Lists a testimonial or creates a Testimonial model instance.
    """
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class TestimonialRetrieve(generics.RetrieveAPIView):
    """
    Retrieves a Testimonial model instance based on id.
    """
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
