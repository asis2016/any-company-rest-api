from rest_framework import generics

from .models import Testimonial
from .serializers import TestimonialSerializer


class TestimonialListCreateAPIView(generics.ListCreateAPIView):
    """
    Lists a testimonial or creates a Testimonial model instance.
    """
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class TestimonialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates or destroy a Testimonial model instance based on id.
    """
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
