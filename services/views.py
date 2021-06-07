from django.views.generic import ListView
from rest_framework import generics

from .models import Service
from .serializers import ServiceSerializer


class ServiceListView(ListView):
    """ Service list view. """
    model = Service
    template_name = 'services/index.html'
    context_object_name = 'services'


class ServiceList(generics.ListAPIView):
    """ Service list API. """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceRetrieve(generics.RetrieveAPIView):
    """ Service detail API. """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
