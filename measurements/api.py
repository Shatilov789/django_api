from rest_framework import generics
from rest_framework.response import Response
from measurements.serializers import ProjectModelSerializers
from measurements.models import Project, Measurement


class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializers
