from rest_framework import generics

from .models import Project
from .serializers import ProjectSerializer


class ProjectList(generics.ListAPIView):
    """ Project list API. """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveAPIView):
    """ Project retrive API. """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
