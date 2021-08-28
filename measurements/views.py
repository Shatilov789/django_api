from rest_framework.viewsets import ModelViewSet

from measurements.models import Project, Measurement
from measurements.serializers import ProjectModelSerializers, MeasurementModelSerializers


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта
    queryset =  Project.objects.all()
    serializer_class =  ProjectModelSerializers

class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
    queryset =  Measurement.objects.all()
    serializer_class =  MeasurementModelSerializers