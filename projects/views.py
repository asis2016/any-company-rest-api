from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# class ProjectList(generics.ListAPIView):
#    """ Project list API. """
#    queryset = Project.objects.all()
#    serializer_class = ProjectSerializer


# class ProjectDetail(generics.RetrieveAPIView):
#    """ Project retrive API. """
#    queryset = Project.objects.all()
#    serializer_class = ProjectSerializer
